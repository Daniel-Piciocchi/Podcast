from main import db, ma
from models import genre

# @add_schema
class Podcast(db.Model):
    __tablename__ = 'podcasts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(500))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genre = db.relationship('Genre', backref='podcast')

    def __repr__(self):
        return f"<podcast {self.id}>"


class PodcastSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Podcast
            fields = ('id', 'title', 'description', 'image_url')
            load_instance = True