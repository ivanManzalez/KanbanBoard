import random
import string
import os, os.path
from test_tasks import Data
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

# get tasks w/ status = todo
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_todos(self):
        tasks = [
            {'title': 'API Call - GET DB Data', 'status': 'todo'},
            {'title': 'Frontend - Advanced CSS Styling - Kanban', 'status': 'todo'},
            {'title': 'Fullend - Backlog Screen', 'status': 'todo'},
            {'title': 'API Call - Create New Task Modal', 'status': 'todo'},
            {'title': 'Frontend - View Task Details', 'status': 'todo'},
            {'title': 'Backend - Optimize delivery', 'status': 'todo'},
        ]
        return {'tasks': tasks}
# get tasks w/ status = in progress   
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_in_progs(self):
        tasks = [
            {'title': 'Backend - Create DB Schema', 'status': 'in_prog'},
        ]
        return {'tasks': tasks}
# get tasks w/ status = done
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_dones(self):
        tasks = [
        {'title':'API call - To Do Tasks', 'status':'done'}, 
        {'title':'API call - In Progress Tasks', 'status':'done'}, 
        {'title':'API call - Done Tasks', 'status':'done'}, 
        {'title':'Styling - Simple Task Buckets', 'status':'done'}, 
        {'title':'HTML - Kanban Structure', 'status':'done'}, 
        {'title':'Frontend - Drag&Drop Tasks', 'status':'done'}, 
        {'title':'Frontend - Modal Popup', 'status':'done'}
        ]
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