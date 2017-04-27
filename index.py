# -*- coding:utf_8 -*-
import web
import os
import re
import base64

import CmdAPI

urls = (
    '/', 'Index',
    '/admin', 'Admin',
    '/login', 'Login',
    '/user', 'User'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
web.config.debug=False
application = web.application(urls, globals())

def checkAuth(auth):
    if auth is None:
        return False
    auth_sub = re.sub('^Basic', '', auth)
    username, password = base64.decodestring(auth_sub).split(':')
    if username in CmdAPI.users and CmdAPI.users[username] == password:
        return True
    else:
        return False

def currentUser(auth):
    if auth is None:
        return None
    auth_sub = re.sub('^Basic', '', auth)
    return base64.decodestring(auth_sub).split(':')[0]

class Index:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        if not checkAuth(auth):
            raise web.seeother('/login')
        else:
            raise web.seeother('/user')

class Admin:
    def GET(self):
        return self.POST()

    def POST(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        if not checkAuth(auth):
            raise web.seeother('/login')
        user = currentUser(auth)
        if user != CmdAPI.ADMIN:
            raise web.seeother('/user')
        i = web.input(op=None)
        try:
            if i.op and i.bot:
                if i.op == 'stop':
                    CmdAPI.stopBot(i.bot)
                elif i.op == 'start':
                    CmdAPI.startBot(i.bot)
            bots = CmdAPI.getBots()
            asf_status = dict()
            for bot in bots:
                asf_status[bot] = CmdAPI.refreshInfo(bot)['Bots'][bot]
            return render.admin(bots, asf_status)
        except CmdAPI.ASFAPIError as e:
            return render.admin(bots, {}, errorName=e.kind, errorInfo=e.detail)


class User:
    def GET(self):
        return self.POST()

    def POST(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        if not checkAuth(auth):
            raise web.seeother('/login')
        i = web.input(op=None)
        try:
            user = currentUser(auth)
            if i.op:
                if i.op == 'stop':
                    CmdAPI.stopBot(user)
                elif i.op == 'start':
                    CmdAPI.startBot(user)
            asf_status = CmdAPI.refreshInfo(user)
            if user in asf_status['Bots']:
                return render.user(user, asf_status['Bots'][user], type)
            else:
                return render.user(user, None, type)
        except CmdAPI.ASFAPIError as e:
            return render.user(user, e.kind, type)

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            if checkAuth(auth):
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Login ASF-Naive-WUI"')
            web.ctx.status = '401 Unauthorized'
        return render.login('Please login.')

if __name__ == "__main__":
    application.run()
