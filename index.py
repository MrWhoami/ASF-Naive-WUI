# -*- coding:utf_8 -*-
import web
import os
import re
import base64

import CmdAPI

urls = (
    '/', 'Index',
    '/login', 'Login'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
web.config.debug=False
application = web.application(urls, globals()).wsgifunc()

class Index:
    def __init__(self):
        pass

    def GET(self):
        return self.POST()

    def POST(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is None:
            raise web.seeother('/login')
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

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic', '', auth)
            username, password = base64.decodestring(auth).split(':')
            if username in CmdAPI.users and CmdAPI.users[username] == password:
                raise web.seeother('/')
            else:
                return render.login('Login failed.')
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Login ASF-Naive-WUI"')
            web.ctx.status = '401 Unauthorized'
        return render.login('Please login.')

if __name__ == "__main__":
    application.run()
