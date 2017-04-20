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
web.config.debug=False

class Index:
    def __init__(self):
        pass

    def GET(self):
        return self.POST()

    def POST(self):
        i = web.input(op=None, bot=None)
        try:
            if i.op and i.bot:
                if i.op == 'stop':
                    CmdAPI.stopBot(i.bot)
                elif i.op == 'start':
                    CmdAPI.startBot(i.bot)
            asf_status = CmdAPI.refreshInfo()
            bots = CmdAPI.getBots()
            return render.index(bots, asf_status['Bots'])
        except CmdAPI.ASFAPIError as e:
            return render.index(bots, {}, errorName=e.kind, errorInfo=e.detail)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
