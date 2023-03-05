from flask import Blueprint, jsonify, request
from main import db
from models.podcast import Podcast, PodcastSchema


podcast = Blueprint('podcast', __name__)

# The GET routes endpoint
@podcast.route("/podcast", methods=["GET"])
def get_podcasts():
    podcasts = Podcast.query.all()
    podcast_schema = PodcastSchema(many=True)
    result = podcast_schema.dump(podcasts)
    return jsonify(result)

@podcast.route("/podcast", methods=["POST"])
def create_podcast():
    podcast_schema = PodcastSchema()
    data = request.json
    errors = podcast_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    podcast = podcast_schema.load(data)
    db.session.add(podcast)
    db.session.commit()
    result = podcast_schema.dump(podcast)
    return jsonify(result), 201

@podcast.route("/podcast/<int:id>", methods=["DELETE"])
def delete_podcast(id):
    podcast = Podcast.query.get(id)
    if not podcast:
        abort(404, description='Podcast not found')
    db.session.delete(podcast)
    db.session.commit()
    podcast_schema = PodcastSchema()
    result = podcast_schema.dump(podcast)
    return jsonify(result)