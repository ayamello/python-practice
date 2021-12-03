from datetime import datetime
from flask.json import jsonify
from app.models.lead_model import LeadModel
from flask import current_app, request
import re

def list_leads():
    leads = LeadModel.query.order_by(LeadModel.visits.desc()).all()
    if leads == []:
        return {"error": "no data found"}, 404
    else:
        return jsonify(leads), 200

def create_lead():
    keys_lead = ['name', 'email', 'phone']

    data = request.json
    keys_from_data = list(data.keys())

    if set(keys_lead) != set(keys_from_data):
        return {"error": "Incorrect fields."}, 404

    if current_app.db.session.query(LeadModel).filter_by(email=data['email']).scalar() is not None:
        return {"error": "email already registered."}, 409
    if current_app.db.session.query(LeadModel).filter_by(phone=data['phone']).scalar() is not None:
        return {"error": "phone already registered."}, 409
    if not re.fullmatch(r'^\([1-9]{2}\)(?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$', data['phone']):
        return {"error": "invalid phone format"}

    lead = LeadModel(**data)

    current_app.db.session.add(lead)
    current_app.db.session.commit()

    return jsonify(lead), 201

def delete_lead():
    key_lead = ['email']
    data = request.json
    keys_from_data = list(data.keys())

    if set(key_lead) != set(keys_from_data):
        return {"error": "Incorrect fields."}, 404

    lead = current_app.db.session.query(LeadModel).filter_by(email=data['email']).scalar()

    if lead is None:
        return {"error": "no data found"}, 404

    current_app.db.session.delete(lead)
    current_app.db.session.commit()

    return jsonify(lead), 200

def update_lead():
    key_lead = ['email']
    data = request.json
    keys_from_data = list(data.keys())

    if set(key_lead) != set(keys_from_data):
        return {"error": "Incorrect fields."}, 404

    lead = LeadModel.query.filter_by(email=data['email']).first()
    
    if lead is None:
        return {"error": "no data found"}, 404

    lead.visits = lead.visits + 1
    lead.last_visit = datetime.now()
    current_app.db.session.commit()

    updated_lead = LeadModel.query.filter_by(email=data['email']).first()

    return jsonify(updated_lead), 200
