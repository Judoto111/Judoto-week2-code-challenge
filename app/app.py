from flask import Flask
from models import db  # Import the database and models

# Initialize the Flask application
app = Flask(__name__)
# Configure the database URI (using SQLite in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
# Disable track modifications to save memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object with the app
db.init_app(app)

# Import and register the routes (API endpoints)
from routes import main
app.register_blueprint(main)

# Main block to run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables based on the models
    app.run(debug=True)  # Run the app in debug mode
