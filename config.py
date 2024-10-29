import os
from flask import Flask
from flask_restful import Api, Resource  # Added Resource import here
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Database configuration (use environment variable)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)

# Initialize the database with the app
db.init_app(app)

# Example model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Example resource
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        return {"username": user.username} if user else {"message": "User not found"}, 404

api.add_resource(UserResource, '/users/<int:user_id>')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
