import os
import re
import cv2
import json
import easyocr
import imutils
import numpy as np
from enum import Enum
from datetime import datetime
from hashlib import sha512
from flask import Flask, request, Response
from flask_cors import CORS
from sqlalchemy import create_engine
from werkzeug.datastructures import MultiDict


app = Flask(__name__)
# app.config["debug"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})


hash_key = "parking_project"


@app.route("/", methods=["GET"])
def default():
    return json.dumps("This is the default page")


@app.route("/api/register/", methods=["POST"])
def register():
    """
        An api endpoint for registering a user

        POST:
            Required args:
                firstname: str
                lastname: str
                email: str
                password: str
                phone: str
                ccCode: str

            Returns:
                ResponseCode: HTTP code to describe finish state

    """
    args = MultiDict(request.get_json())

    required = ["firstname", "lastname",
                "email", "password", "phone", "ccCode"]

    # Check if all required arg keys are present
    if not all(arg in required for arg in args):
        return Response("", ResponseCodes.inv_syntax.value)

    state = insert("INSERT INTO users ([firstname], [lastname], [email], [password], [phone], [ccCode]) VALUES ('{fname}', '{lname}', '{email}', '{encrypted}', '{phone}', '{ccCode}')".format(
        fname=args.get("firstname"),
        lname=args.get("lastname"),
        email=args.get("email").lower(),
        encrypted=hash_password(args.get("password")),
        phone=args.get("phone"),
        ccCode=args.get("ccCode")
    ))

    return Response("", state.value)


@app.route("/api/login/", methods=["GET"])
def login():
    """
        An api endpoint for logging in as an existing user

        GET:
            Required args:
                email: str
                password: str

            user_data: 
            {
                firstname: str,
                lastname: str,
                email: str,
                phone: str,
                ccCode: str
            }

            Returns:
                ResponseCode: HTTP code to describe finish state
                    Successful: user_data
    """

    args = request.args

    required = ["email", "password"]

    if not all(arg in required for arg in args):
        return Response("", ResponseCodes.inv_syntax.value)

    user = select("SELECT [password] from users WHERE email='{email}'".format(
        email=args.get("email").lower()
    ))

    if isinstance(user, ResponseCodes):
        return Response("", user.value)

    if len(user) != 1:
        return Response("No user linked to email", ResponseCodes.no_email.value)

    password = user[0][0]

    if hash_password(args.get("password")) != password:
        return Response("Invalid password", ResponseCodes.inv_pwd.value)

    user = select("SELECT [userId], [firstname], [lastname], [email], [phone], [ccCode] FROM users WHERE [email]='{email}' and [password]='{password}'".format(
        email=args.get("email").lower(),
        password=hash_password(args.get("password"))
    ))

    if isinstance(user, ResponseCodes):
        return Response("", user.value)

    if len(user) != 1:
        return Response("", ResponseCodes.inv_pwd.value)

    formatted = format_result(
        user, ["userId", "firstname", "lastname", "email", "phone", "ccCode"])

    return Response(json.dumps(formatted[0]), ResponseCodes.success.value)


@app.route("/api/areas/", methods=["POST", "GET"])
def areas():
    """
        An api endpoint to insert and extract parking areas

        POST:
            Required args:
                areaName: str
                address: str
                latitude: float
                longitude: float

            Returns:
                ResponseCode: HTTP code to describe finish state

        GET:
            Required args:
                None

            area_data:
            [
                {
                    areaId: int,
                    areaName: str,
                    address: str,
                    latitude: float,
                    longitude: float
                }
            ]

            Returns:
                ResponseCode: HTTP code to describe finish state
                    Successful: area_data

    """

    if request.method == "POST":

        args = MultiDict(request.get_json())
        required = ["areaName", "address", "latitude", "longitude"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax.value)

        state = insert("INSERT INTO Areas ([areaName], [address], [latitude], [longitude]) VALUES ('{areaName}', '{address}', {latitude}, {longitude})".format(
            areaName=args.get("areaName"),
            address=args.get("address"),
            latitude=args.get("latitude"),
            longitude=args.get("longitude")
        ))

        return Response("", state.value)

    else:

        areas = select(
            "SELECT [areaId], [areaName], [address], [latitude], [longitude] FROM areas")

        if isinstance(areas, ResponseCodes):
            return Response("", areas.value)

        formatted = format_result(
            areas, ["areaId", "areaName", "address", "latitude", "longitude"])
        return Response(json.dumps(formatted), ResponseCodes.success.value)


@app.route("/api/regLicenseplates/", methods=["POST", "GET"])
def reg_licenseplates():
    """
        An api endpoint that lets you register a new licenseplate and look up all plates for a specific user

        POST:
            Required args:
                licenseplate: str
                brand: str
                model: str
                type: str

            Returns:
                ResponseCode: HTTP code to describe finish state

        GET: 
            Required args:
                None

            car_data:
            [
                {
                    licenseplate: str,
                    brand: str,
                    model: str,
                    type: str
                }
            ]

            Returns: 
                ResponseCode: HTTP code to describe finish state
                    Successful: car_data
    """

    if request.method == "POST":

        args = MultiDict(request.get_json())
        required = ["licenseplate", "brand", "model", "type"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax.value)

        state = insert("INSERT INTO RegisteredLicenseplates([licenseplate], [brand], [model], [type]) VALUES ('{licenseplate}', '{brand}', '{model}', '{type}')".format(
            licenseplate=args.get("licenseplate"),
            brand=args.get("brand"),
            model=args.get("model"),
            type=args.get("type")
        ))

        return Response("", state.value)
    else:

        licenseplates = select(
            "SELECT [licenseplate], [brand], [model], [type] FROM registeredLicenseplates")

        if isinstance(licenseplates, ResponseCodes):
            return Response("", licenseplates.value)

        formatted = format_result(
            licenseplates, ["licenseplate", "brand", "model", "type"])

        return Response(json.dumps(formatted), ResponseCodes.success.value)


@app.route("/api/userLicenseplates/", methods=["POST", "GET"])
def user_licenseplate():
    """
        An api endpint that lets you set a saved licenseplate for a specific user as well as reading it

        POST:
            Required args:
                userId: str
                licenseplate: str

            Returns:
                ResponseCode: HTTP code to describe finish state

        GET:
            Required args:
                userId: str

            licenseplate_data:
            [
                {
                    licenseplate: str,
                    brand: str,
                    model: str,
                    type: str
                }
            ]


            Returns:
                ResponseCode: HTTP code to describe finish state
                    Successful: licenseplate_data
    """

    if request.method == "POST":

        args = MultiDict(request.get_json())

        required = ["userId", "licenseplate"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax.value)

        state = insert("INSERT INTO userLicenseplates (userId, licenseplate) VALUES ({userId}, '{licenseplate}')".format(
            userId=args.get("userId"),
            licenseplate=args.get("licenseplate")
        ))

        return Response("", state.value)

    else:
        args = request.args

        required = ["userId"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax.value)

        licenseplates = select(
            "SELECT [rl].[licenseplate], [rl].[brand], [rl].[model], [rl].[type] FROM userLicenseplates as ul INNER JOIN RegisteredLicenseplates as rl ON rl.licenseplate = ul.licenseplate WHERE userId={userId}".format(
                userId=args.get("userId")
            ))

        if isinstance(licenseplates, ResponseCodes):
            return Response("", licenseplates.value)

        formatted = format_result(
            licenseplates, ["licenseplate", "brand", "model", "type"])

        return Response(json.dumps(formatted), ResponseCodes.success.value)


@app.route("/api/parkings/", methods=["POST", "GET"])
def parkings():
    """
        An api endpoint for extracting and inserting a parking

        POST:
            Required args:
                licenseplate: str
                userId: int
                areaId: int
                minutes: int
                price: int
                state: str
                timestamp: str

            Returns:
                ResponseCode: HTTP code to describe finish state

        GET:
            Required args:
                userId: int

            parking_data:
            [
                {
                    licenseplate: str,
                    userId: int,
                    areaId: int,
                    minutes: int,
                    price: int,
                    state: str,
                    timestamp: str
                }
            ]


            Returns:            
                ResponseCode: HTTP code to describe finish state
                    Successful: parking_data
    """

    if request.method == "POST":

        args = MultiDict(request.get_json())

        required = ["licensePlate", "userId", "areaId",
                    "minutes", "price", "state", "timestamp"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax.value)

        state = insert("INSERT INTO parkings ([licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp]) VALUES('{licenseplate}', {userId}, {areaId}, {minutes}, {price}, '{state}', '{timetamp}')".format(
            licenseplate=args.get("licenseplate"),
            userId=args.get("userId"),
            minutes=args.get("minutes"),
            price=args.get("price"),
            state=args.get("state"),
            timetamp=args.get("timetamp")
        ))

        return Response("", state.value)

    else:
        args = request.args

        optional = ["userId"]

        if not all(arg in optional for arg in args):
            query = "SELECT [licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp] FROM parkings WHERE userId={userId}".format(
                userId=args.get("userId")
            )
        else:
            query = "SELECT [licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp] FROM parkings"

        areas = select(query)

        if isinstance(areas, ResponseCodes):
            return Response("", areas.value)

        formatted = format_result(
            areas, ["licenseplate", "userId", "areaId", "minutes", "price", "state", "timestamp"])

        return Response(json.dumps(formatted), ResponseCodes.success.value)


@app.route("/api/detectLicenseplate/", methods=["GET"])
def detect_licenseplate():

    filestr = request.files["file"]

    file_bytes = np.fromstring(filestr.read(), np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)

    keypoints = cv2.findContours(
        edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:50]

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)

        mask = np.zeros(gray.shape, np.uint8)
        cv2.drawContours(mask, [approx], 0, 255, -1)
        cv2.bitwise_and(img, img, mask=mask)

        try:
            (x, y) = np.where(mask == 255)
            (x1, y1) = (np.min(x), np.min(y))
            (x2, y2) = (np.max(x), np.max(y))
            cropped_image = gray[x1:x2+1, y1:y2+1]
        except ValueError as e:
            print(e)
            continue

        # print("moved past")
        reader = easyocr.Reader(['en'])
        result = reader.readtext(cropped_image)

        if len(result) != 0:
            formatted = result[-1][-2].replace(" ", "")
            if len(formatted) > 5 and any(char.isdigit() for char in formatted):
                # print(len(approx))
                break

    plate = result[-1][-2].replace(" ", "")
    regex = re.compile('[^a-zA-Z0-9]')

    licenseplate = regex.sub('', plate)

    # formatted = format_result((licenseplate,), ["licenseplate"])

    return Response(json.dumps({"licenseplate": licenseplate}), ResponseCodes.success.value)


def insert(query: str):
    """
        A function to make sure that the inersted query in fact is an insert query

        Returns:
            int: Based on if insert was successful
    """

    if "insert" not in query.lower() or any(keyword in query.lower() for keyword in ["delete", "drop", "alter"]):
        return ResponseCodes.inv_syntax

    db_engine = connect()
    try:
        with db_engine.begin() as conn:
            conn.exec_driver_sql(query)
    except Exception as e:
        print(f"This is the exception {e}")
        return ResponseCodes.failed_query

    return ResponseCodes.success


def select(query: str):
    """
        A function to make sure that the inersted query in fact is a select query

        Returns:
            List: Fetched result from db
    """
    if "select" not in query.lower() or any(keyword in query.lower() for keyword in ["insert", "delete", "drop", "alter"]):
        return ResponseCodes.inv_syntax

    db_engine = connect()

    try:
        with db_engine.begin() as conn:
            result = conn.exec_driver_sql(query).all()
    except Exception as e:
        print(e)
        return ResponseCodes.failed_query

    return result


def connect():
    """
        Reads db config file and opens a connection to the database.

        Returns:
            sqlalchemy.engine: A connection to the database
    """

    with open(os.path.join("./backend", "db_config.json"), "rt") as file:
        config = json.load(file)
        conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(
            config["conn"].format(**config))

    return create_engine(conn_str)


def format_result(data: list[tuple], keys: list[str]):
    """
        Formats all data inputs from tuple to dict with selected keys

        Example:
            data = [(1, 2, 3), (4, 5, 6)]
            keys = ["key1", "key2", "key3"]

            result = [
                {"key1": 1, "key2": 1, "key3": 3},
                {"key1": 4, "key2": 5, "key3": 6},
            ]

        Args:
            data (list): A list of tuples return from database
            keys (list): A list of keys that match 1:1 with data indices

        Returns:
            list: A list of dict with selected key, value pairs

    """

    formatted = [{k: format_val(k, v)
                  for k, v in zip(keys, row)} for row in data]

    return formatted


def format_val(k, v):
    """
        Converts value into an int or float if possible

        Args:
            k (str): a string key
            v (str): a string input 

        Returns:
            str: Converted input if possible to 
    """

    types = [int, float, str]

    for type in types:
        if is_convertable(k, v, type):
            return type(v)


def is_convertable(key: str, val: str, data_type):
    """
        Takes two arguments and checks if the selected value is convertable to the selected type

        Args:
            key: (str) a specific key that is checked for
            val: (str) a specific value to check for
            type: (any) a specific type to check for

        Returns:
            bool: Whether or not the value is convertable
    """
    try:
        if key in ["phone"] and data_type != str:
            return False

        data_type(str(val))
        return True
    except ValueError:
        return False


def format_datetime(datetime: datetime):
    """
        Converts a datetime object to a string

        Args:
            datetime (Datetime): A timestamp

        Returns:
            str: Timestamp as a string
    """
    return datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def hash_password(password: str):
    """
        Generates a hashed key from selected parameter

        Args:
            password (str): a password that needs to be hashed

        Returns:
            str: The hashed value from selected password
    """
    return sha512(f"{repr(password)},{hash_key}".encode("utf-8")).hexdigest()


class ResponseCodes(Enum):
    """
        200 - success:       A successful call to DB
        400 - failed_query:  Query was not allowed to execute
        401 - inv_pwd:       Password did not corresepond with a user
        403 - inv_syntax:    Query contained some invalid syntax
        406 - no_email:      Email did not belong to a user
    """
    success = 200
    failed_query = 400
    inv_pwd = 401
    inv_syntax = 403
    no_email = 406

# def main(a, b):
    # app.run()

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)