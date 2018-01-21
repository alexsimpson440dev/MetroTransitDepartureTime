# MetroTransitDepartureTime
The Metro Transit Departure Time application will provide information to users for when their next bus is scheduled to leave a desired bus stop. The user is able to select their route name, desired bus stop name, and the direction they would like to be traveling.

The application is written in Python, Flask, HTML, and CSS. The application is also hosted on Heroku.com under the address of: metrotransit-timeuntildepart.herokuapp.com

If you were going to download this application, you would need python 3.6, pip to install packages for ease, and you would need to install all of the packages that are program has in its requirments file. (Not actually all of them, but most)

Once all requirements are met, run app.py. This will load the application on a local server.

I have two different testing files in the application. One for the API, one for the Server. Those are both under the directory /tests

Once the application is running, it will display all available routes, choose one and click next. The next page will display the available directions this route will lead. Choose one and click next. The following page will display all of the available bus stops for your choosen route, and direction. Choose one and click next. The final page will then display the amount of minutes until the next bus will depart from the bus stop you chose. The final page also displays a Home link to redirect you back to the home page.

If you forget to select a choice from any of the scroll menus, the program will display a message of what you did not select, and redirect you to the home page.

Pages used for sources:
- http://svc.metrotransit.org/
- http://flask.pocoo.org/docs/0.12/
- http://jinja.pocoo.org/docs/2.10/
- https://docs.python.org/3.6/library/datetime.html
