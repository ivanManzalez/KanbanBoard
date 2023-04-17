import random
import string
import os, os.path
from my_data import Data
import urllib.parse #to parse dynamic data in php
import json 
####################################
import cherrypy
#http://127.0.0.1:8080/


class ToDo(object):

# Cherry py takes the name of the method 
# as url name (index = '/')

# must define query parameters in method name definition

    @cherrypy.expose
    def index(self):
        # define business logic here 
        # call business logic from external file
        return open('views/todo.html').read().format(
            data= Data
            )

    @cherrypy.expose
    def kanban(self):
        # define business logic here 
        # call business logic from external file
        return open('views/todo_kanban.html')

    @cherrypy.expose
    def backlog(self, length=0):
        # define business logic here 
        # call business logic from external file
      return open('views/todo_backlog.html')

# API Endpoints
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_tasks(self):
        tasks = ['Alice', 'Bob', 'Charlie', 'Daniel', 'Eric', 'Freddy', 'Georgina']
        return {'tasks': tasks}
    
    @cherrypy.expose
    def add_task(self, task, description):
        try:
            # code to add task to database
            success_message = "Task added successfully"
            return json.dumps({'success': False, 'message': success_message})
        
        except:
            error_message = "Failed to add task"
            return json.dumps({'success': False, 'message': error_message})

# CherryPy Tutorial
    @cherrypy.expose
    ##override default argument by using ?key=value in url
    def generate(self, length=8):
        # define business logic here 
        # call business logic from external file
        return ''.join(random.sample(string.hexdigits, int(length)))

####################################
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

####################################
    cherrypy.quickstart(ToDo(), '/', conf)






















####################################