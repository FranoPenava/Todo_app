from flask import Flask, render_template, request
from common.database import Database
from main.routes import main

app = Flask(__name__)

app.register_blueprint(main)

@app.before_first_request
def db():
    Database.initialize()


