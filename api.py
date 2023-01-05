import json
from flask import Flask, request
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["debug"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})

# @app.route("/api/", methods=["GET", "POST"])


def select(query):

    if "select" not in query.lower():
        return []
    
    engine = connect()

    with engine.begin() as conn:
        result = conn.exec_driver_sql
    

def connect():
    """
        Reads db config file and opens a connection to the database.

        Returns:
            sqlalchemy.engine: A connection to the database
    """
    with open("./db_config.json", "r") as file:
        config = json.load(file)
        conn_str = conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(config["conn"].format(**config))
        
    return create_engine(conn_str)

