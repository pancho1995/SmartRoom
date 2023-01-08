from flask import Blueprint, jsonify, request, make_response
from src.constants.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from src.database import Relations, Names, db, create_item_models
from src.database import User
from sqlalchemy import func
from flasgger import swag_from

devices = Blueprint("devices", __name__, url_prefix="/api/v1/devices")

energy_types = {'active_import_energy': 'ACTIVEIMPORTID', 'active_export_energy': 'ACTIVEEXPORTID', 
                'reactive_import_energy': 'REACTIVEIMPORTID', 'reactive_export_energy': 'REACTIVEEXPORTID',  
                'apparent_import_energy': 'APPARENTIMPORTID', 'apparent_export_energy': 'APPARENTEXPORTID'}

@devices.get('/alldevices')
@swag_from('./docs/devices/get_all.yml')
def get_all():

    name=Names.query.all()

    return jsonify(devices=[i.serialize for i in name]), HTTP_200_OK

#select time from item0001 where time = (select max(time) from item0001 where time <= '2021-12-01 02:47:00');
#select * from item00+

@devices.post('/getlastmeasurements')
@swag_from('./docs/devices/last_measurement.yml')
def last_measurement():
    ID=request.json.get('id', '')
    measurement=request.json.get('measurement', '')
    start_time=request.json.get('start_time', '')
    end_time=request.json.get('end_time', '')

    if start_time >= end_time:
        response = make_response(jsonify({
            'error': 'The start time is greater than end time'
        }))
        response.status_code=HTTP_400_BAD_REQUEST
    else: 
        names=Names.query.filter_by(ID=ID).first()
        if names:
            if measurement in energy_types:
                relations = Relations.query.filter_by(ID=ID).first()
                col_name = energy_types[measurement]
                
                id = relations.serialize[col_name]

                if id:
                    item = create_item_models('item00'+str(id))
                    query = item.query.filter(item.TIME >= start_time, item.TIME <= end_time).all()
                    response = make_response(jsonify(lastMeasurements=[i.serialize for i in query]))
                    response.status_code=HTTP_200_OK
                else:
                    response = make_response(jsonify({'error': 'The measurement was not found'}))
                    response.status_code=HTTP_404_NOT_FOUND
        else: 
            response = make_response(jsonify({'error': 'Wrong id'}))
            response.status_code = HTTP_400_BAD_REQUEST
    return response
