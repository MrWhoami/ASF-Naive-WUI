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

    def GET(self):
        i = web.input()
        try:
            CmdAPI.refreshInfo()
            render.index(CmdAPI.asf_status['Bots'])
        except CmdAPI.ASFAPIError e:
            render.index({}, errorName=e.kind, errorInfo=e.detail)
        return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
