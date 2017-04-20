# -*- coding:utf_8 -*-

import subprocess as subp
import json
import os

# Some global variables
CMDHEAD = []

# Some classes
class ASFAPIError(Exception):
    """Base exception in this module"""
    def __init__(self, kind, detail=None):
        self.kind = kind
        self.detail = detail
    def __str__(self):
        return str(self.kind)

# Functions
def cmd(command):
    """Command wrap and send"""
    global CMDHEAD
    real_cmd = CMDHEAD
    real_cmd.append(command)
    rawout = None
    try:
        rawout = subp.check_output(real_cmd)
        if "ERROR" in rawout:
            raise ASFAPIError("ASF Error", detail=rawout)
    except subp.CalledProcessError:
        raise ASFAPIError("Command Error", detail=rawout)
    return rawout

def refreshInfo():
    """Call api command of the ASF"""
    global respTime, asf_status
    rawout = cmd('api')
    wcf_resp = rawout.splitlines()[-1]
    resp_time = wcf_resp.split('|')[0]
    try:
        start_pos = wcf_resp.index('{')
    except ValueError:
        print wcf_resp
	raise
    raw_json = wcf_resp[start_pos:]
    asf_status = json.loads(raw_json)
    if type(asf_status) != type(dict()):
        print rawout
        raise TypeError("Need dict for parse result, but get {}".format(str(type(asf_status))))
    return asf_status

def pauseBot(bot_name):
    rawout = cmd('pause {0}'.format(bot_name))

def resumeBot(bot_name):
    rawout = cmd('resume {0}'.format(bot_name))

# Init some variables when being imported
if os.name == 'nt':
    CMDHEAD = ['..\\ASF.exe', '--client']
elif os.name == 'posix':
    CMDHEAD = ['mono', '../ASF.exe', '--client']
else:
    raise ASFAPIError('Unknown system', detail=os.name)

if __name__ == "__main__":
	asf_status = refreshInfo()
	print asf_status
