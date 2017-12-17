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
def home():
    if request.method=='GET':
        routes = API.get_routes()
        return render_template('index.html', routes=routes)
    else:
        return render_template('index.html')

# runs the server locally
if __name__ == "__main__":
    app.run(port=9999, debug=True)