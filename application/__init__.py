from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///categories.db"
app.config["SQLALCHEMY_ECHO"] = True
# SQLALCHEMY_TRACK_MODIFICATIONS would add significant overhead, so it is disabled.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from application import views

from application.categories import models
from application.categories import views

db.create_all()
