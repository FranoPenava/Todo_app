from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from common.database import Database

# File for storing my routes!

# Cretaing blueprint
main = Blueprint("main", __name__)

# Creating my basic route for returning all of the previous data I typed! 
@main.route("/")
def index():
    todos = Database.find({})
    return render_template("home.html", todos = todos)

# Route for adding infromation I type!
@main.route("/add_todo", methods = ["POST"])
def add_todo():
    # Gettin that item!
    todo_item = request.form.get("add-todo")
    
    # Storing into my db!
    json = {"add": todo_item, "complete": False}
    Database.insert(data = json)
    return redirect(url_for("main.index"))

# Route for marking the completed ones!
@main.route("/complete_todo/<oid>")
def complete_todo(oid):
    # Finding the item by ObjectId!
    todo_item = Database.find_one({"_id": ObjectId(oid)})
    item = todo_item["add"]
    # Creating my own json with same data except now complete is equal to true!
    json = {
        "_id": ObjectId(oid),
        "add": item,
        "complete": True
    }
    # Repalcing new json with the existing one!
    Database.replace_one(todo_item, json)
    return redirect(url_for("main.index"))

# Delete data with value true off complete!
@main.route("/delete_completed")
def delete_completed():
    Database.remove({"complete": True})
    return redirect(url_for("main.index"))

# deleting all items!
@main.route("/delete_all")
def delete_all():
    Database.remove({})
    return redirect(url_for("main.index"))