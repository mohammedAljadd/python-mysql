from flask import Flask, app
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config.from_object("config.Myconfig")
mysql = MySQL(app)


from app import application