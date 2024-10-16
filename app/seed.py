import csv
from models import db, Episode, Guest, Appearance
from app import app


with app.app_context():
    db.drop_all()  
    db.create_all()  
    
    
    with open('seed_data/episodes.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            episode = Episode(
                date=row['date'],
                number=row['number']
            )
            db.session.add(episode)
    
    
    with open('seed_data/guests.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            guest = Guest(
                name=row['name'],
                occupation=row['occupation']
            )
            db.session.add(guest)
    
    db.session.commit()  
    print("Database seeded successfully!")
