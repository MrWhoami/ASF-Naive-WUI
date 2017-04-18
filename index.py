# -*- coding:utf_8 -*-
import web
import os

import CmdAPI

urls = (
    '/', 'Index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class Index:
    def __init__(self):
        pass

    def generateWebpage(self):
        try:
            CmdAPI.refreshInfo()
            return render.index(CmdAPI.asf_status['Bots'])
        except CmdAPI.ASFAPIError e:
            return render.index({}, errorName=e.kind, errorInfo=e.detail)

    def POST(self):
        i = web.input(op=None, bot=None)
        try:
            if op and bot:
                if op == 'pause':
                    CmdAPI.resumeBot(bot)
                elif op == 'start':
                    CmdAPI.pauseBot(bot)
            CmdAPI.refreshInfo()
            return render.index(CmdAPI.asf_status['Bots'])
        except CmdAPI.ASFAPIError e:
            return render.index({}, errorName=e.kind, errorInfo=e.detail)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
