from app import app, mysql
from flask import render_template, request, redirect
from app.utils import *


 


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/user-db", methods=["GET", "POST"])
def user_db():

    if request.method == "POST":
        
        req = request.form
        email = req.get("email")
        password = request.form["password"]
        db(mysql, email, password)
        

    return redirect("/home")