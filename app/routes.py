from flask import Blueprint, jsonify, request, abort
from .models import db, Episode, Guest, Appearance


main = Blueprint('main', __name__)

@main.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(include_appearances=True))

@main.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@main.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    if rating is None or not (1 <= rating <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    episode = Episode.query.get(data['episode_id'])
    guest = Guest.query.get(data['guest_id'])

    if not episode or not guest:
        return jsonify({"errors": ["Invalid episode or guest ID"]}), 400

    appearance = Appearance(
        rating=rating,
        episode_id=episode.id,
        guest_id=guest.id
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201
