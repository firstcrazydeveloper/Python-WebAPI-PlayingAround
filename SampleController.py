# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:23:40 2020

@author: abhishekar
"""

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        return {'Method': 'Employees'} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        result = {'data': 'SampleData'}
        return result

class Employees_Name(Resource):
    def get(self, employee_id):
        result = {'data':'Abhishek'}
        return result
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
      # app.run(port='5020')
     # app.run('localhost', 5220)
     app.run(host='0.0.0.0', port='4200')