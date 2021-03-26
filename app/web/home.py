#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    return "Hi home page"
