import inspect
import os
import cherrypy
from mako.lookup import TemplateLookup
from kendoDAO.AdherentsDAO import AdherentsDAO
from service.ServiceAdherent import ServiceAdherent

try:
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
except NameError :
    __file__ = inspect.getfile(inspect.currentframe())
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
print (_curdir)



webDir = os.path.join(_curdir, 'web')
myTemplatesDir = os.path.join(webDir,'views/templates')
myModulesDir = os.path.join(webDir,'views/templates/mako_modules')
mylookup = TemplateLookup(directories=[myTemplatesDir], module_directory=myModulesDir,
                          output_encoding='utf-8',
                          encoding_errors='replace')

#------------------------------------------------------------
# Templates HTML
#------------------------------------------------------------
_pageListAdherent = mylookup.get_template("adherents.mako.html")
_pageDetailsAdherent = mylookup.get_template("details.adherent.mako.html")

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        gestionadherent = AdherentsDAO()
        return _pageListAdherent.render(adherents=gestionadherent.findAll())
    @cherrypy.expose
    def details(self, licence):
        gestionadherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionadherent.findById(licence))
        return _pageDetailsAdherent.render(adherent=serviceAdherent.adherent, grades=serviceAdherent.adherent.grades)

if __name__ == '__main__':

    global_conf = {
        'global': { 'autoreload.on': False,
			'server.socket_host': '127.0.0.1',
			'server.socket_port': 8080,
			'server.protocol_version': 'HTTP/1.1',
                            'server.thread_pool' : 5,
                            'tools.encode.encoding' : "Utf-8",
                            'environment': 'production',
                            'log.error_file': 'site.log',
                            'log.screen': True}}
    cherrypy.config.update(global_conf)

    conf_appli = {'/static': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(webDir, 'static')},
            '/static/templates': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': myTemplatesDir},
            '/static/tmp/mako_modules': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': myModulesDir},
            '/static/css': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(webDir, 'static/css'),
                            'tools.staticdir.content_types': {'css': 'text/css'}},
            '/static/images': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(webDir, 'static/images'),
                            'tools.staticdir.content_types': {'jpg': 'image/jpg'}},
            '/static/js': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(webDir, 'static/js'),
                      'tools.staticdir.content_types': {'js': 'application/javascript'}}}

    # Démarrer le serveur HTTP CherryPy
    cherrypy.quickstart(HelloWorld(), '/', config=conf_appli)