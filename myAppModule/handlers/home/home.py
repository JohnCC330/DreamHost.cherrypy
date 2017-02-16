import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Home(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='home.index.html')
    def index(self):
        return {
            'msg': 'This is our message to the world!'
        }
