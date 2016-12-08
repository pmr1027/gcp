from flask import Flask, render_template, render_template_string, make_response, redirect
from flask.flask_restful import Api, Resource, reqparse, abort

import json
import string
import random
from datetime import datetime
import dateutil.parser as dparser

class Test(Resource):
    def get(self):
        return "Hello World!!!!!!!"

#####################################################################

# Assign URL paths to our resources.
app = Flask(__name__)
api = Api(app)

#Businesses
api.add_resource(Test, '/test')



# Redirect from the index to the list of help requests.
@app.route('/')
def index():
    return redirect(api.url_for(Test), code=303)


# This is needed to load JSON from Javascript running in the browser.
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.template_filter('datetime')
def format_datetime(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime('%B %d, %Y at %I:%M%p')
app.jinja_env.filters['datetime'] = format_datetime

@app.template_filter('getDate')
def format_getDate(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
app.jinja_env.filters['getDate'] = format_getDate

@app.template_filter('getTime')
def format_getTime(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime('%H:%M')
app.jinja_env.filters['getTime'] = format_getTime

# Start the server.
#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8888, debug=True)
