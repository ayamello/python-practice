from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LeadModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "lead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False, unique=True)
    creation_date = db.Column(db.DateTime, default=datetime.now)
    last_visit = db.Column(db.DateTime, default=datetime.now)
    visits = db.Column(db.Integer, default=1)
    