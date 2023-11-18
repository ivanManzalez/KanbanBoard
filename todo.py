import random
import string
import os, os.path

from data import Data
from db.tasks.task import Task
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
            data= Data()
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

    ####### API Endpoints ############

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_todos(self):
        data = Data()
        tasks = data.get_tasks(task_status="To Do")
        # print("TODOs:",tasks)
        return {'tasks': tasks}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_in_progs(self):
        data = Data()
        tasks = data.get_tasks(task_status="In Progress")
        # print("In Progress:",tasks)
        return {'tasks': tasks}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_dones(self):
        data = Data()
        tasks = data.get_tasks(task_status="Completed")
        # print("Completed:",tasks)
        return {'tasks': tasks}


    ##################################

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_all(self):
        data = Data()
        tasks = data.get_all()
        print("All Tasks:",tasks)
        return {'tasks': tasks}
    
    @cherrypy.expose
    def add_task(self, title, description, urgency, importance, status):
        print("add_task")
        try:
            data = Data()
            task = {
                "title"      :title, 
                "description":description, 
                "urgency"    :urgency, 
                "importance" :importance, 
                "status"     :status
                }
            created_task = data.create_new_task(task)
            
            if(created_task["status"] == 500):
                error_message = f"Failed to add task - {created_task['error']}"
                return json.dumps({'success': False, 'message': error_message, 'status':created_task["status"]})
            success_message = f"Task #{created_task['data']} added successfully"

            return json.dumps({'success': True, 'message': success_message, "task":created_task["data"]}) #'task':created_task
        
        except Exception as e:
            print("\n\nERROR\n\n")
            error_message = json.dumps({'error': e})
            cherrypy.response.status = 400  # Set the status code
            return json.dumps({'success': False, 'message': error_message})


    @cherrypy.expose
    def update_task(self, identifier, title, description, urgency, importance, status):
        print("update_task")
        try:
            data = Data()
            task = {
                "task_id"    :identifier,
                "title"      :title, 
                "description":description, 
                "urgency"    :urgency, 
                "importance" :importance, 
                "status"     :status
                }
            updated_task = data.update_existing_task(task)
            
            if(updated_task["status"] == 500):
                error_message = f"Failed to update task - {updated_task['error']}"
                return json.dumps({'success': False, 'message': error_message, 'status':updated_task["status"]})

            success_message = f"{updated_task['data']} task(s) updated successfully"

            return json.dumps({'success': True, 'message': success_message, "task":updated_task["data"]})
        
        except Exception as e:
            print("\n\nERROR\n\n")
            error_message = json.dumps({'error': e})
            print(e)
            cherrypy.response.status = 400  # Set the status code
            return json.dumps({'success': False, 'message': error_message})

    @cherrypy.expose
    # @cherrypy.tools.json_in()
    def delete_task(self, identifier):
        print("identifier",identifier)
        try:
            data = Data()
            deleted_task = data.delete_existing_task(task_id=identifier)
            
            if(deleted_task["status"] == 500):
                error_message = f"Failed to add task: {deleted_task['error']}"
                return json.dumps({'success': False, 'message': error_message, 'status':deleted_task["status"]})

            success_message = f"Task #{identifier} deleted successfully"

            return json.dumps({'success': True, 'message': success_message, "task":deleted_task}).encode('utf-8')
        
        except Exception as e:
            print("\n\nERROR\n")
            error_message = json.dumps({'error': e})
            cherrypy.response.status = 400  # Set the status code
            return json.dumps({'success': False, 'message': error_message}).encode('utf-8')

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
            },
        '/delete_task': {
            'request.methods_with_bodies': ['DELETE'],
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
    }
        }

    cherrypy.quickstart(ToDo(), '/', conf)

####################################