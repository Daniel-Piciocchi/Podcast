from controllers.user_controller import user
from controllers.episode import episode
from controllers.podcast import podcast
from controllers.rating import rating
from controllers.genre import genre


registerable_controllers = [
    user,
    podcast,
    genre,
    episode,
    rating
]
