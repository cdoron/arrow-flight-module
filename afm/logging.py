#
# Copyright 2020 IBM Corp.
# SPDX-License-Identifier: Apache-2.0
#

import sys
from loguru import logger

def init_log():
    logger.remove()
    logger.level("TRACE", icon="<magenta>TRC</magenta>")
    logger.level("ERROR", icon="<light-red><bold>ERR</bold></light-red>")
    logger.level("INFO", icon="INF", color="<green>")
    logger.add(sink=sys.stderr, format = "{time:HH:mm} {level} QQQ {file}:{line} > {message}", colorize=True)
    #logger.add(sink=sys.stderr, format = "<light-black>{time:HH:mm}</light-black> {level.icon} {file}:{line} <cyan>></cyan> {message}")
    #prefix = "<light-black>{time:HH:mm}</light-black> "
    #postfix = " {file}:{line} <cyan>></cyan> {message}"
    #logger.add(sink=sys.stderr, level='TRACE', format = prefix + "<magenta>TRC</magenta>" + postfix)
    #logger.add(sink=sys.stderr, level='DEBUG', format = prefix + "<yellow>DBG</yellow>" + postfix)
    #logger.add(sink=sys.stderr, level='INFO', format = prefix + "<green>INF</green>" + postfix)
    #logger.add(sink=sys.stderr, level='WARNING', format = prefix + "<red>WRN</red>" + postfix)
    #logger.add(sink=sys.stderr, level='ERROR', format = prefix + "<light-red><bold>ERR</bold></light-red>" + postfix)
    #logger.add(sink=sys.stderr, level='CRITICAL', format = prefix + "<light-red><bold>FTL</bold></light-red>" + postfix)
