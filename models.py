from app import db
#a class that defines the venue table
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    facebook_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String())
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

    #debugging statements when printing the objects
    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User {0}>'.format(self.name)
