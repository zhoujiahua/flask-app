#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_cors import CORS
from app.models.user import db


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)

    # 第一种DB创建方式
    # db.create_all(app=app)

    # 第二种DB创建方式
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    # Web register
    from app.web.user import web_user
    from app.web.home import web_home
    app.register_blueprint(web_user)
    app.register_blueprint(web_home)

    # Api register
    from app.api.user import api_user
    from app.api.comm import api_comm
    app.register_blueprint(api_user)
    app.register_blueprint(api_comm)
