import json
from hashlib import sha512
from flask import Flask, request
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
        return False

    insert("INSERT INTO users (firstname, lastname, email, password, phone, country) VALUES ({fname},{lname},{email},{encrytped},{phone},{country})".format(
        {
            "fname": args.get("firstname"),
            "lname": args.get("lastname"),
            "email": args.get("email"),
            "encrypted": hash_password(args.get("password")),
            "phone": args.get("phone"),
            "country": args.get("country"),
        }
    ))

    return


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
        return 1

    db_engine = connect()

    with db_engine.begin() as conn:
        conn.exec_driver_sql(query)

    return 0


def select(query):
    """
        A function to make sure that the inersted query in fact is a select query

        Returns:
            List: Fetched result from db
    """
    if "select" not in query.lower():
        return []

    db_engine = connect()

    with db_engine.begin() as conn:
        result = conn.exec_driver_sql(query).all()

    return result


def connect():
    """
        Reads db config file and opens a connection to the database.

        Returns:
            sqlalchemy.engine: A connection to the database
    """
    with open("./db_config.json", "rt") as file:
        config = json.load(file)
        conn_str = conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(
            config["conn"].format(**config))

    return create_engine(conn_str)


def hash_password(password: str):
    return sha512(f"{repr(password)},{hash_key}".encode("utf-8")).hexdigest()


app.run(host="0.0.0.0", port=5050)
