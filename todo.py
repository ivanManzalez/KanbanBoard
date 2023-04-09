####################################
import cherrypy
#http://127.0.0.1:8080/

class ToDo(object):
    
    @cherrypy.expose
    def index(self):
        return open('views/todo.html')

    @cherrypy.expose
    def kanban(self):
      return open('views/todo_kanban.html')
    
    @cherrypy.expose
    def backlog(self):
      return open('views/todo_backlog.html')

    # @cherrypy.expose
    # def index(self):
    #     return "Hello world!"

    # @cherrypy.expose
    # def generate(self):
    #     return ''.join(random.sample(string.hexdigits, 8))
    


if __name__ == '__main__':
    cherrypy.quickstart(ToDo())
























####################################