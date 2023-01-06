import json
from hashlib import sha512
from flask import Flask, request, Response
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["debug"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})

hash_key = "parking_project"

# @app.route("/api/", methods=["GET", "POST"])


@app.route("/api/register/", methods=["POST"])
def register():

    args = request.args

    required = ["firstname", "lastname",
                "email", "password", "phone", "country"]

    # Check if all required arg keys are present
    if not all(arg in required for arg in args):
        return Response("", 400)

    state = insert("INSERT INTO users (firstname, lastname, email, password, phone, countrycode) VALUES ('{fname}', '{lname}', '{email}', '{encrypted}', '{phone}', '{country}')".format(
        fname=args.get("firstname"),
        lname=args.get("lastname"),
        email=args.get("email"),
        encrypted=hash_password(args.get("password")),
        phone=args.get("phone"),
        country=args.get("country")
    ))

    return Response("", state)


@app.route("/api/login/", methods=["GET"])
def login():

    args = request.args

    required = ["email", "password"]

    if not all(arg in required for arg in args):
        return Response("", 400)

    user = select("SELECT [firstname], [lastname], [email], [phone] FROM users WHERE [email] = '{email}' and [password] = '{password}'".format(
        email=args.get("email"),
        password=hash_password(args.get("password"))
    ))

    if len(user) != 1:
        return Response("", 401)

    formatted = format_result(
        user, ["firstname", "lastname", "email", "phone"])

    return json.dumps(formatted[0])


@app.route("/api/countries/", methods=["GET"])
def countries():

    countries = select("SELECT [country], [phonecode], [name] FROM countries")

    formatted = format_result(countries, ["country", "phonecode", "name"])

    return json.dumps(formatted)


@app.route("/api/areas/", methods=["GET"])
def areas():

    areas = select(
        "SELECT [areaId], [areaName], [address], [langitude], [longitude] FROM areas")

    formatted = format_result(
        areas, ["areaId", "areaName", "address", "langitude", "longitude"])

    return json.dumps(formatted)


@app.route("/api/regLicenseplates/", methods=["GET"])
def reg_licenseplates():

    areas = select(
        "SELECT [licenseplate], [brand], [model], [type] FROM registeredLicenseplate")

    formatted = format_result(
        areas, ["licenseplate", "brand", "model", "type"])

    return json.dumps(formatted)


@app.route("/api/userLicenseplates/", methods=["GET"])
def user_licenseplate():

    args = request.args

    required = ["userId"]

    if not all(arg in required for arg in args):
        return Response("", 400)

    licenseplates = select(
        "SELECT [userId], [licenseplates] FROM userLicenseplates WHERE userId={userId}".format(
            userId=args.get("userId")
        ))

    formatted = format_result(
        licenseplates, ["userId", "licenseplates"])

    return json.dumps(formatted)


@app.route("/api/parkings/", methods=["POST", "GET"])
def parkings():

    args = request.args

    if request.method == "POST":
        required = ["licensePlate", "userId", "areaId",
                    "minutes", "price", "state", "timestamp"]

        if not all(arg in required for arg in args):
            return Response("", 400)

        return

    else:
        required = ["userId"]

        if not all(arg in required for arg in args):
            return Response("", 400)

        areas = select("SELECT [licenseplate], [userId], [areaId], [minutes], [price], [state], [timestamp] FROM parkings WHERE userId = '{userId}'".format(
            userId=args.get("userId")
        ))

        formatted = format_result(
            areas, ["licenseplate", "userId", "areaId", "minutes", "price", "state", "timestamp"])

        return json.dumps(formatted)


@app.route("/api/test/", methods=["GET"])
def test():
    print(hash_password("This is a test password"))

    return json.dumps("test")


def insert(query):
    """
        A function to make sure that the inersted query in fact is an insert query

        Returns:
            int: Based on if insert was successful
    """

    if "insert" not in query.lower():
        return 400

    db_engine = connect()
    try:
        with db_engine.begin() as conn:
            conn.exec_driver_sql(query)
    except Exception as e:
        print(e)
        return 401

    return 200


def select(query):
    """
        A function to make sure that the inersted query in fact is a select query

        Returns:
            List: Fetched result from db
    """
    if "select" not in query.lower():
        return []

    db_engine = connect()

    try:
        with db_engine.begin() as conn:
            result = conn.exec_driver_sql(query).all()
    except Exception as e:
        print(e)
        return []

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


def format_result(data, keys):

    formatted = [{k: format_val(v) for k, v in zip(keys, row)} for row in data]

    return formatted


def format_val(v):

    if is_convertable(v, int):
        return int(v)

    elif is_convertable(v, float):
        return float(v)
    else:
        return v


def is_convertable(val, type):
    try:
        type(val)
        return True
    except:
        return False


def hash_password(password: str):
    return sha512(f"{repr(password)},{hash_key}".encode("utf-8")).hexdigest()


app.run(host="0.0.0.0", port=5050)
