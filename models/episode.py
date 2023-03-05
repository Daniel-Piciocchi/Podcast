from main import db
from models import rating

class Episode(db.Model):
    __tablename__ = 'episode'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000))
    audio_url = db.Column(db.String(500))
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcasts.id'))
    podcast = db.relationship('Podcast', backref='episode')
    rating_id = db.Column(db.Integer, db.ForeignKey('ratings.id'))
    rating = db.relationship('Rating', backref='episode')


    def __repr__(self):
        return f"<episode {self.id}>"
