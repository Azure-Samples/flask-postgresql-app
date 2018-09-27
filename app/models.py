from app import db


class Guest(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    partysize = db.Column(db.Integer, default=1)

    def __init__(self, name=None, email=None, partysize=1):
        self.name = name
        self.email = email
        self.partysize = partysize or 1