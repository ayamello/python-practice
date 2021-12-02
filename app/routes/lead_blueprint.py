from flask import Blueprint
from app.controllers.lead_controller import delete_lead, list_leads, create_lead, update_lead

bp = Blueprint('bp_lead', __name__, url_prefix='/leads')

bp.get("")(list_leads)
bp.post("")(create_lead)
bp.patch("")(update_lead)
bp.delete("")(delete_lead)
