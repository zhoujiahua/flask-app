#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import jsonify
from . import api_comm

@api_comm.route("/api/comm/email")
def api_comm_email():
    return 'send email api'

@api_comm.route("/api/comm/search/<key>/<content>")
def api_comm_search(key,content):
    search_data = {'key':key, 'content':content}
    return jsonify(search_data)