from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LeadModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: datetime
    last_visit: datetime
    visits: int

    __tablename__ = 'lead'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.Date())
    last_visit = db.Column(db.Date())
    visits = db.Column(db.Integer, default=1)
    