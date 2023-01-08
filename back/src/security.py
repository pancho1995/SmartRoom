from flask import Blueprint, jsonify, request, make_response
from src.constants.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from src.database import Relations, Names, db, create_item_models
from src.database import User
from sqlalchemy import func
from flasgger import swag_from

security = Blueprint("security", __name__, url_prefix="/api/v1/security")

@security.get('/door')
@swag_from('./docs/security/security_devices.yml')
def door_status():

    door_opened = True
    return jsonify(door_opened), HTTP_200_OK

@security.get('/alarm')
@swag_from('./docs/security/security_devices.yml')
def alarm():

    door_opened = True
    return jsonify("Ringe ringe"), HTTP_200_OK
