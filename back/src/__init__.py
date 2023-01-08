from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db
from src.devices import devices
from src.security import security
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger, swag_from
from src.config.swagger import template,swagger_config

#Application Factory
def create_app(test_config=None):

    app=Flask(__name__,
    instance_relative_config=True)


    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            SWAGGER = {
                'title':"DSD Back API",
                'uiversion':3
            }
        )

    else:
        app.config.from_mapping(test_config)

    
    db.app=app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    app.register_blueprint(devices)
    app.register_blueprint(security)

    Swagger(app, config=swagger_config,
    template=template)

    return app
