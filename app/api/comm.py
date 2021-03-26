#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import request, jsonify
from . import api_comm

@api_comm.route("/api/comm/email")
def api_comm_email():
    return 'send email api'

@api_comm.route("/api/comm/search/<key>/<content>")
def api_comm_search(key,content):
    return jsonify({'key':key, 'content':content})

@api_comm.route("/api/comm/news")
def api_comm_news():
    page = request.args['page']
    limit = request.args['limit']
    return jsonify({'page':page, 'limit':limit})