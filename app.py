from src.metrotransit_api import MetroTransitAPI
API = MetroTransitAPI()

route = "Brklyn Center - Fremont - 26th Av - Chicago - MOA"
direction = 4
stop = "Portland Ave and 77th St"
route_number = API.get_route_number(route)
print(route_number)
stop_id = API.get_stop_identifier(stop, direction, route_number)
print(stop_id)
departure_time = API.get_next_departure(stop_id, route_number, direction)
print(departure_time)

