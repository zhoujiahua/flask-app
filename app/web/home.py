#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from . import home

@home.route("/")
def home_page():
    return "Hi home page"
