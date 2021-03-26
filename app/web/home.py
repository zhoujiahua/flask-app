#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from . import web_home

@web_home.route("/")
def web_home_page():
    return "Hi home page"
