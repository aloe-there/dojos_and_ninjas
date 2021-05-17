from flask import render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def new_ninja():
    return render_template("create_ninja.html", dojos = Dojo.get_all())

@app.route("/ninjas/add", methods=["POST"])
def add_ninja():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": int(request.form["age"]),
        "dojo_id": int(request.form["dojo_id"])
    }
    Ninja.add(data)
    return redirect(f"/dojos/{data['dojo_id']}")