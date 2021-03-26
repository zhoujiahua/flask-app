#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from . import api_comm

@api_comm.route("/api/comm/email")
def api_comm_email():
    return 'send email api'