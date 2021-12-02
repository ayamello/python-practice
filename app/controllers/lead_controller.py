from flask.json import jsonify
from app.models.lead_model import LeadModel
from flask import current_app

def list_leads():
    leads = LeadModel.query.order_by(LeadModel.visits.desc()).all()
    if leads == []:
        return {"error": "no data found"}, 404
    else:
        return jsonify(leads), 200

def create_lead():
    # lead1 = {
    #     "name": "Mello",
    #     "email": "mello@gmail.com",
    #     "phone": "71998451232",
    #     "visits": 2
    # }

    # lead = LeadModel(**lead1)

    # current_app.db.session.add(lead)
    # current_app.db.session.commit()
    return jsonify(), 201

def delete_lead():
    return 'oi'

def update_lead():
    return 'oi'