from flask import Blueprint, jsonify, request, abort
from models import db, Episode, Guest, Appearance

# Create a blueprint for organizing routes
main = Blueprint('main', __name__)

@main.route('/episodes', methods=['GET'])
def get_episodes():
    # Retrieve all episodes from the database
    episodes = Episode.query.all()
    # Serialize episodes to JSON format and return
    return jsonify([episode.to_dict() for episode in episodes])

@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    # Retrieve a specific episode by ID
    episode = Episode.query.get(id)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404
    # Return the episode details along with its appearances
    return jsonify(episode.to_dict(include_appearances=True))

@main.route('/guests', methods=['GET'])
def get_guests():
    # Retrieve all guests from the database
    guests = Guest.query.all()
    # Serialize guests to JSON format and return
    return jsonify([guest.to_dict() for guest in guests])

@main.route('/appearances', methods=['POST'])
def create_appearance():
    # Get JSON data from the request body
    data = request.get_json()

    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    # Validate the rating
    if rating is None or not (1 <= rating <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400
    
    if episode_id is None or guest_id is None:
        return jsonify({"errors": ["episode_id and guest_id are required"]}), 400

    # Check if episode and guest exist
    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({"errors": ["Invalid episode or guest ID"]}), 400

    # Create and add new appearance
    appearance = Appearance(
        rating=rating,
        episode_id=episode.id,
        guest_id=guest.id
    )

    db.session.add(appearance)
    try:
        db.session.commit()  # Commit changes to the database
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Unable to create appearance", str(e)]}), 500

    # Return the newly created appearance as JSON
    return jsonify(appearance.to_dict()), 201
