from flask import render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def home_page():
    return render_template("index.html", dojos = Dojo.get_all())

@app.route("/dojos/<int:id>")
def show_dojo_ninjas(id):
    return render_template("dojo_ninjas.html", dojo=Dojo.get(id), ninjas=Ninja.get_all_from_dojo(id))

@app.route("/dojos/add", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.add(data)
    return redirect("/dojos")