from flask import Flask, request, redirect, render_template, flash, url_for
from src.metrotransit_api import MetroTransitAPI
import os

# sets API to the metro transit api
API = MetroTransitAPI()

# sets app to flask items and sets secret key
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = os.environ['SECRET']

# all routes are checking to see if the user is adding the correct items
# if they do not, then they are going to be redirected back to the main home page

# all routes provide a new title and desired items to be displayed on the page

# gets index.html
# if the get function is run, the home function gets routes from the API and displays it in a web page
@app.route('/')
@app.route('/index.html')
def home():
    title = "Home"
    desired_item = "Please Select Your Desired Route"

    routes = API.get_routes()
    return render_template('index.html', routes=routes, directions=None, bus_stops=None, time=None,
                           desired_item=desired_item, title=title)

# direction route gets /direction
# gets the route number from url and inputs it into API
# returns the directions in a dictionary along with their value
@app.route('/direction', methods=['get'])
def direction():
    try:
        title = "Direction"
        desired_item = "Please Select Your Desired Direction"

        route_number = request.args.get('route')
        directions = API.get_directions(route_number)

        return render_template('index.html', routes=None, directions=directions, route_number=route_number,
                               bus_stops=None, time=None, desired_item=desired_item, title=title)
    except TypeError:
        flash('Please Select a Route!')
        return redirect(url_for('home'))

# stop route gets route number and direction number from url
# inputs those values into API
# API then returns the bus stops and their bus stop identifier
@app.route('/stop', methods=['get'])
def stop():
    try:
        title = "Bus Stop"
        desired_item = "Please Select Your Desired Bus Stop"

        route_number = request.args.get('route')
        direction_number = request.args.get('direction')

        bus_stops = API.get_stop_identifier(direction_number, route_number)
        return render_template('index.html', routes=None, directions=None, bus_stops=bus_stops,
            route_number=route_number, direction_number=direction_number, time=None, desired_item=desired_item, title=title)
    except TypeError:
        flash('Please Select a Direction!')
        return redirect(url_for('home'))

# time route gets route number, direction number, and stop number from url
# the API then inputs those numbers in and returns the time until that bus will departure from information given
@app.route('/time', methods=['get'])
def time():
    try:
        title = "Departure Time"
        desired_item = "Your Next Bus Will Depart In:"

        route_number = request.args.get('route')
        direction_number = request.args.get('direction')
        stop_number = request.args.get('stop')

        time = API.get_next_departure(route_number, direction_number, stop_number)
        if stop_number is None:
            flash('Please Select a Bus Stop!')
            return redirect(url_for('home'))
        elif time is None:
            flash('Sorry, no more Buses are leaving this location!')
            return redirect(url_for('home'))
        else:
            return render_template('index.html', routes=None, directions=None, bus_stops=None,
                                   time=time, desired_item=desired_item, title=title)
    except TypeError:
        return redirect(url_for('home'))

# runs the server locally
if __name__ == "__main__":
    app.run(port=9999, debug=True)