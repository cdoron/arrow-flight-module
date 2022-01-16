#
# Copyright 2020 IBM Corp.
# SPDX-License-Identifier: Apache-2.0
#
import logging
import json_log_formatter
import time

FybrikAppUUID = 'app.fybrik.io/app-uuid'
Level         = 'level'
Message       = 'message'
Time          = 'time'
Caller        = 'caller'
FuncName      = 'funcName'

logger = logging.getLogger('arrow-flight-module')
app_uuid = ''

class FybrikFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra[Message] = message
        extra[Level] = record.levelname
        extra[Caller] = record.filename + ':' + str(record.lineno)
        extra[FuncName] = record.funcName
        extra[Time] = time.ctime(record.created)
        extra[FybrikAppUUID] = app_uuid
        return extra

def init_logger(loglevel_arg, app_uuid_str):
    global app_uuid
    app_uuid = app_uuid_str
    loglevel = getattr(logging, loglevel_arg, logging.WARNING)
    logger.setLevel(loglevel)
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    ch.setFormatter(FybrikFormatter())
    logger.addHandler(ch)