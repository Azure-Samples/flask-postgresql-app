from app import DB

class Guest(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'guests'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    email = DB.Column(DB.String(120))
    partysize = DB.Column(DB.Integer, default=1)

    def __init__(self, name=None, email=None, partysize=1):
        self.name = name
        self.email = email
        self.partysize = partysize
    