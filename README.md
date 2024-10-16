# Late Show

## Description
Late Show is a Flask web application that allows users to manage episodes, guests, and their appearances on the show. Users can view episodes and guests, as well as create new appearances for guests in specific episodes. The application uses SQLite for database management and supports RESTful API endpoints.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Judoto111/Judoto-week2-code-challenge.git
Navigate into the project directory:
bash
Copy code
cd Judoto-week2-code-challenge
Set up a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
To run the application, use the following command:

bash
Copy code
flask run
Once the server is running, you can access the application at http://127.0.0.1:5000.

API Endpoints
GET /episodes: Retrieve a list of all episodes.
GET /episodes/<id>: Retrieve details for a specific episode by ID.
GET /guests: Retrieve a list of all guests.
POST /appearances: Create a new appearance for a guest in an episode.
Features
View all episodes and guests.
Retrieve detailed information about specific episodes.
Create appearances for guests in different episodes, including rating their performance.
Contributing
Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Authors
Doreen Chepkoech - Initial work