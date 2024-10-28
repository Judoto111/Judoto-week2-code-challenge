
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object for ORM
db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'  # Name of the table in the database
    
    # Unique identifier for each episode
    id = db.Column(db.Integer, primary_key=True)
    # The air date of the episode
    date = db.Column(db.String, nullable=False)
    # The episode number
    number = db.Column(db.Integer, nullable=False)
    
    # Relationship to the Appearance model (one-to-many)
    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete-orphan")

    def to_dict(self, include_appearances=False):
        # Serialize the Episode object into a dictionary
        episode_dict = {
            "id": self.id,
            "date": self.date,
            "number": self.number
        }
        if include_appearances:
            # Include appearances in the serialized output if requested
            episode_dict["appearances"] = [
                appearance.to_dict() for appearance in self.appearances
            ]
        return episode_dict

class Guest(db.Model):
    __tablename__ = 'guests'  # Name of the table in the database
    
    # Unique identifier for each guest
    id = db.Column(db.Integer, primary_key=True)
    # Name of the guest
    name = db.Column(db.String, nullable=False)
    # Occupation of the guest
    occupation = db.Column(db.String, nullable=False)

    # Relationship to the Appearance model (one-to-many)
    appearances = db.relationship('Appearance', back_populates='guest', cascade="all, delete-orphan")

    def to_dict(self):
        # Serialize the Guest object into a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'  # Name of the table in the database
    
    # Unique identifier for each appearance
    id = db.Column(db.Integer, primary_key=True)
    # Rating given for the appearance, must be between 1 and 5
    rating = db.Column(db.Integer, nullable=False)
    # Foreign key referencing the Episode this appearance is associated with
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    # Foreign key referencing the Guest this appearance is associated with
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Relationship back to the Episode model
    episode = db.relationship('Episode', back_populates='appearances')
    # Relationship back to the Guest model
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict(self):
        # Serialize the Appearance object into a dictionary
        return {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id,
            "episode": self.episode.to_dict(),  # Include episode details
            "guest": self.guest.to_dict()       # Include guest details
        }
