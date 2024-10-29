import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # Update URI as needed
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Set up naming conventions for foreign keys
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)

# Initialize the app with SQLAlchemy
db.init_app(app)

# Import your models here to avoid circular imports
from models import Episode, Guest, Appearance

# Define your resources and API setup here...
# (e.g., from flask_restful import Api, Resource)
# api = Api(app)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
