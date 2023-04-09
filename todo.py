import random
import string
from my_data import Data
####################################
import cherrypy
#http://127.0.0.1:8080/


class ToDo(object):

# Cherry py takes the name of the method 
# as url name (index = '/')

    @cherrypy.expose
    def index(self):
        return open('views/todo.html').read().format(
            data= Data
            )

    @cherrypy.expose
    def kanban(self):
      return open('views/todo_kanban.html')
    
    @cherrypy.expose
    def backlog(self):
      return open('views/todo_backlog.html')

    @cherrypy.expose
    ##override default argument by using ?key=value in url
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.quickstart(ToDo())
























####################################