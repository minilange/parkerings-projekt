import json
from enum import Enum
from datetime import datetime
from hashlib import sha512
from flask import Flask, request, Response
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["debug"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})

hash_key = "parking_project"


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

    args = request.args

    required = ["firstname", "lastname",
                "email", "password", "phone", "ccCode"]

    # Check if all required arg keys are present
    if not all(arg in required for arg in args):
        return Response("", ResponseCodes.inv_syntax)

    state = insert("INSERT INTO users ([firstname], [lastname], [email], [password], [phone], [ccCode]) VALUES ('{fname}', '{lname}', '{email}', '{encrypted}', '{phone}', '{ccCode}')".format(
        fname=args.get("firstname"),
        lname=args.get("lastname"),
        email=args.get("email"),
        encrypted=hash_password(args.get("password")),
        phone=args.get("phone"),
        country=args.get("ccCode")
    ))

    return Response("", state)


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
        return Response("", ResponseCodes.inv_syntax)

    user = select("SELECT [passowrd] from users WHERE email='{email}'".format(
        email=args.get("email")
    ))

    if isinstance(int, user):
        return Response("", user)

    if len(user) != 1:
        return Response("", ResponseCodes.no_email)

    password = user[0]

    if hash_password(args.get("password")) != password:
        return Response("", )

    user = select("SELECT [firstname], [lastname], [email], [phone], [ccCode] FROM users WHERE [email]='{email}' and [password]='{password}'".format(
        email=args.get("email"),
        password=hash_password(args.get("password"))
    ))

    if isinstance(int, user):
        return Response("", user)

    if len(user) != 1:
        return Response("", ResponseCodes.inv_pwd)

    formatted = format_result(
        user, ["firstname", "lastname", "email", "phone", "ccCode"])

    return Response(json.dumps(formatted[0]), ResponseCodes.success)


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

        args = request.args
        required = ["areaName", "address", "latitude", "longitude"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        state = insert("INSERT INTO Areas ([areaName], [address], [latitude], [longitude]) VALUES ('{areaName}', '{address}', {latitude}, {longitude})".format(
            areaName=args.get("areaName"),
            address=args.get("address"),
            latitude=args.get("latitude"),
            longitude=args.get("longitude")
        ))

        return Response("", state)

    else:

        areas = select(
            "SELECT [areaId], [areaName], [address], [langitude], [longitude] FROM areas")

        if isinstance(int, areas):
            return Response("", areas)

        formatted = format_result(
            areas, ["areaId", "areaName", "address", "langitude", "longitude"])
        return Response(json.dumps(formatted), ResponseCodes.success)


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

        args = request.args
        required = ["licenseplate", "brand", "model", "type"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        state = insert("INSERT INTO RegisteredLicenseplates([licenseplate], [brand], [model], [type]) VALUES ('{licenseplate}', '{brand}', '{model}', '{type}')".format(
            licenseplate=args.get("licenseplate"),
            brand=args.get("brand"),
            model=args.get("model"),
            type=args.get("type")
        ))

        return Response("", state)
    else:

        licenseplates = select(
            "SELECT [licenseplate], [brand], [model], [type] FROM registeredLicenseplate")

        if isinstance(int, licenseplates):
            return Response("", licenseplates)

        formatted = format_result(
            licenseplates, ["licenseplate", "brand", "model", "type"])

        return Response(json.dumps(formatted), ResponseCodes.success)


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
                    userId: str,
                    licenseplate: str
                }
            ]


            Returns:
                ResponseCode: HTTP code to describe finish state
                    Successful: licenseplate_data

    """
    args = request.args

    if request.method == "POST":

        required = ["userId", "licenseplate"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        state = insert("INSERT INTO userLicenseplates (userId, licenseplate) VALUES ({userId}, '{licenseplate}')".format(
            userId=args.get("userId"),
            licenseplate=args.get("licenseplate")
        ))

        return Response("", state)

    else:

        required = ["userId"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        licenseplates = select(
            "SELECT [userId], [licenseplate] FROM userLicenseplates WHERE userId={userId}".format(
                userId=args.get("userId")
            ))

        formatted = format_result(
            licenseplates, ["userId", "licenseplate"])

        return Response(json.dumps(formatted), ResponseCodes.success)


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

    args = request.args

    if request.method == "POST":

        required = ["licensePlate", "userId", "areaId",
                    "minutes", "price", "state", "timestamp"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        state = insert("INSERT INTO parkings ([licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp]) VALUES('{licenseplate}', {userId}, {areaId}, {minutes}, {price}, '{state}', '{timetamp}')".format(
            licenseplate=args.get("licenseplate"),
            userId=args.get("userId"),
            minutes=args.get("minutes"),
            price=args.get("price"),
            state=args.get("state"),
            timetamp=args.get("timetamp")
        ))

        return Response("", state)

    else:
        required = ["userId"]

        if not all(arg in required for arg in args):
            return Response("", ResponseCodes.inv_syntax)

        areas = select("SELECT [licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp] FROM parkings WHERE userId={userId}".format(
            userId=args.get("userId")
        ))

        formatted = format_result(
            areas, ["licenseplate", "userId", "areaId", "minutes", "price", "state", "timestamp"])

        return Response(json.dumps(formatted), ResponseCodes.success)


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
        print(e)
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

    with open("./db_config.json", "rt") as file:
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

    formatted = [{k: format_val(v) for k, v in zip(keys, row)} for row in data]

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

    types = [int, float, format_datetime, str]

    for type in types:
        if is_convertable(k, v, type):
            return type(v)


def is_convertable(key: str, val: str, data_type: type):
    """
        Takes two arguments and checks if the selected value is convertable to the selected type

        Args:
            key: (str) a specific key that is checked for
            val: (any) a specific value to check for
            type: (any) a specific type to check for

        Returns:
            bool: Whether or not the value is convertable
    """
    try:
        if key in ["phone", "ccCode"]:
            return False

        if callable(data_type):
            format_datetime(val)

        data_type(val)
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

app.run(host="0.0.0.0", port=5050)
