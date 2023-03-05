from main import db

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    def __repr__(self):
        return f"<rating {self.id}>"
