## Late Show API Documentation

This project is a RESTful API built with Flask-RESTful that manages a database of Episodes, Guests, and Appearances. It allows users to perform various operations, including listing episodes, retrieving specific episode details, and adding new guest appearances.

### Features
1. **Episodes**: Retrieve all episodes or details of a specific episode.
2. **Guests**: List all available guests and their details.
3. **Appearances**: Create new guest appearances for specific episodes.

### Prerequisites
To run this project locally, ensure you have the following installed:
- **Python 3.x**
- **Flask**
- **Flask-RESTful**
- **Flask-SQLAlchemy**
- **Flask-Migrate**

### Installation Steps
1. **Clone the Repository**
   First, clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <project_directory>

2. Set Up the Database 
   app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

  Run database migrations to create tables:
   flask db init
   flask db migrate
   flask db upgrade

3.Seed the Database (Optional) If you have sample data in a CSV file and would like to seed it into the database, use the following command python seed_data.py <path_to_your_csv_file>

4.Running the Server
      python app.py


API Endpoints
1.List All Episodes

GET /episodes
Returns a list of all episodes with their details.

2.Get Episode by ID

GET /episodes/<int:id>
Retrieve details of a specific episode by its ID.


3.List All Guests

GET /guests
Returns a list of all guests with their details.

4.Create New Appearance

POST /appearances
Creates a new appearance for a guest in an episode. You must send the guest ID, episode ID, and rating in the request body.