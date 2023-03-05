from flask import Blueprint, jsonify, request
from main import db
from models.episode import Episode

episode = Blueprint('episode', __name__)

# The GET routes endpoint
@episode.route("/episodes", methods=["GET"])
def get_episode():
    # get all the episode from the database table
    # episode_list = episode.query.all()
    # Convert the episode from the database into a JSON format and store them in result
    #result = episode_schema.dump(episode_list)
    # return the data in JSON format
    #return jsonify(result)
    return "List of episode retrieved"

# The POST route endpoint
@episode.route("/episode", methods=["POST"])
def create_episode():
    # #Create a new episode
    # episode_fields = episode_schema.load(request.json)

    new_episode = Episode()
    # new_episode.title = episode_fields["title"]
    # new_episode.description = episode_fields["description"]
    # new_episode.status = episode_fields["status"]
    # new_episode.priority = episode_fields["priority"]
    # # not taken from the request, generated by the server
    # new_episode.date = date.today()
    # # add to the database and commit
    # db.session.add(new_episode)
    # db.session.commit()
    # #return the episode in the response
    # return jsonify(episode_schema.dump(new_episode))
    return "episode created"


# Finally, we round out our CRUD resource with a DELETE method
@episode.route("/<int:id>/", methods=["DELETE"])
def delete_episode(id):
    # #get the episode id invoking get_jwt_identity
    # episode_id = get_jwt_identity()
    # #Find it in the db
    # episode = episode.query.get(episode_id)
    # #Make sure it is in the database
    # if not episode:
    #     return abort(401, description="Invalid episode")
    # # Stop the request if the episode is not an admin
    # if not episode.admin:
    #     return abort(401, description="Unauthorised episode")
    # # find the episode
    # episode = episode.query.filter_by(id=id).first()
    # #return an error if the episode doesn't exist
    # if not episode:
    #     return abort(400, description= "episode doesn't exist")
    # #Delete the episode from the database and commit
    # db.session.delete(episode)
    # db.session.commit()
    # #return the episode in the response
    # return jsonify(episode_schema.dump(episode))
    return "episode Deleted"