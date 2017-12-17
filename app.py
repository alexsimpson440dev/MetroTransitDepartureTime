from src.metrotransit_api import MetroTransitAPI
from datetime import datetime
API = MetroTransitAPI()

# gets users input to input into the MetroTransitAPI class
route = input("Please enter in a route name: ").lower()
direction = int(input("Please enter in a direction number: "))
stop = input("Please enter in a stop name: ").lower()

# sets the returned input from MetroTransitAPI to variables
# those variables are then input into the API for the next departure time
# the final returned value is returned
route_number = API.get_route_number(route)
stop_id = API.get_stop_identifier(stop, direction, route_number)

# gets the returned time, if applicable, and then prints it
departure_time = API.get_next_departure(route_number, direction, stop_id)
print(departure_time)

