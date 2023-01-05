from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Submission(db.Model):
    
    cik = db.Column(db.String(100), primary_key=True)
    ein = db.Column(db.String(100))
    phone = db.Column(db.String(12))
    description = db.Column(db.String(255))
    name = db.Column(db.String(255))
    entityType = db.Column(db.String(255))
    sic = db.Column(db.String(255))
    sicDescription = db.Column(db.String(255))
    website = db.Column(db.String(255))
    investorWebsite = db.Column(db.String(255))
    category = db.Column(db.String(255))
    fiscalYearEnd = db.Column(db.String(255))
    stateOfIncorporation = db.Column(db.String(3))
    stateOfIncorporationDescription = db.Column(db.String(255))
    fiscalYearEnd = db.Column(db.String(255))
    flags = db.Column(db.String(255))
    
    insiderTransactionForOwnerExists = db.Column(db.Boolean, default=False)
    insiderTransactionForIssuerExists = db.Column(db.Boolean, default=False)
    
    filings = db.Column(JSON)
    addresses = db.Column(JSON)
    tickers = db.Column(JSON)
    exchanges = db.Column(JSON)
    formerNames = db.Column(JSON)

    def __repr__(self):
        return f'<Submission "{self.cik}">'