#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import render_template
from . import web_home


@web_home.route("/")
def web_home_page():
    return render_template('index.html')
