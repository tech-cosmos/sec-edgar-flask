from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cik = db.Column(db.String(150))
    content = db.Column(JSON)

    def __repr__(self):
        return f'<Submission "{self.cik}">'