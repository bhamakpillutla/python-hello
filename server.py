# from flask import Flask, jsonify
# import time

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hi", 200

# if __name__=='__main__':
#     app.run(debug=True,host='0.0.0.0', port = 5050)


from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Welcome to AWS - , " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
