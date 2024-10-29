import csv
from app import app, db  # Import the app and db instance
from models import Episode, Guest  # Import your models

def seed_database():
    # Function to seed the database with initial data
    with app.app_context():  # Ensure we're in the app context
        db.drop_all()  # Clear existing data
        db.create_all()  # Create new tables

        # Seed episodes from a CSV file
        try:
            with open('seed_data/episodes.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    episode = Episode(
                        date=row['date'],  # Read date from CSV
                        number=int(row['number'])  # Convert number to integer
                    )
                    db.session.add(episode)  # Add episode to the session
                db.session.commit()  # Save changes to the database
                print("Episodes seeded successfully!")
        except FileNotFoundError:
            print("Error: 'seed_data/episodes.csv' file not found.")
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred while seeding episodes: {e}")

        # Seed guests from a CSV file
        try:
            with open('seed_data/guests.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    guest = Guest(
                        name=row['name'],  # Read name from CSV
                        occupation=row['occupation']  # Read occupation from CSV
                    )
                    db.session.add(guest)  # Add guest to the session
                db.session.commit()  # Save changes to the database
                print("Guests seeded successfully!")
        except FileNotFoundError:
            print("Error: 'seed_data/guests.csv' file not found.")
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred while seeding guests: {e}")

# Run the seeding function if this script is executed
if __name__ == "__main__":
    seed_database()
