#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.user import user
    from app.web.home import home

    app.register_blueprint(user)
    app.register_blueprint(home)
