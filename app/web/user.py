#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Blueprint, jsonify

user = Blueprint("user", __name__)


@user.route("/user/login")
def user_login():
    return jsonify({"name": "jerry"})
