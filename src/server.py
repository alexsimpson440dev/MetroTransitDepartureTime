from flask import Flask, request, redirect, render_template
from src.metrotransit_api import MetroTransitAPI
import os

# sets API to the metro transit api
API = MetroTransitAPI()

# sets app to flask items and sets secret key
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = os.urandom(24)

# gets index.html
# if the get function is run, the home function gets routes from the API and displays it in a web page
@app.route('/')
@app.route('/index.html')
def home():
    routes = API.get_routes()
    return render_template('index.html', routes=routes, directions=None, bus_stops=None, time=None)

@app.route('/direction', methods=['get', 'post'])
def direction():
    route_number = request.args.get('route')
    directions = API.get_directions(route_number)

    return render_template('index.html', routes=None, directions=directions, route_number=route_number, bus_stops=None, time=None)

@app.route('/stop', methods=['get', 'post'])
def stop():
    route_number = request.args.get('route')
    direction_number = request.args.get('direction')

    bus_stops = API.get_stop_identifier(direction_number, route_number)
    return render_template('index.html', routes=None, directions=None, bus_stops=bus_stops,
    route_number=route_number, direction_number=direction_number, time=None)

@app.route('/time', methods=['get', 'post'])
def time():
    route_number = request.args.get('route')
    direction_number = request.args.get('direction')
    stop_number = request.args.get('stop')

    time = API.get_next_departure(route_number, direction_number, stop_number)
    return render_template('index.html', routes=None, directions=None, bus_stops=None, time=time)

# runs the server locally
if __name__ == "__main__":
    app.run(port=9999, debug=True)