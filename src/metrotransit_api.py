import urllib.request as request
import json

# setting Constant Variables
DEFAULT_URL='http://svc.metrotransit.org/NexTrip/'
JSON_FORMAT='?format=json'

class MetroTransitAPI(object):
    def __init__(self):
        pass

    # defines the get_route_number
    # this returns all route numbers where a users entered in route is in the API's route url
    def get_route_number(self, route):
        routes_url = DEFAULT_URL + "Routes" + JSON_FORMAT
        read_url = self.read_provided_url(routes_url)
        parse_read_url = self.parse_provided_url(read_url)
        for items in parse_read_url:
            if route in items['Description'].lower():
                return items['Route']
            else:
                pass

    # defines the get_stop_identifier which intakes a bus stop name, direction number, and route number
    # the function then returns the bus stop number if applicable
    def get_stop_identifier(self, bus_stop, direction, route_number):
        stops_url = DEFAULT_URL + "Stops/" + str(route_number) + "/" + str(direction) + JSON_FORMAT
        read_url = self.read_provided_url(stops_url)
        parsed_url = self.parse_provided_url(read_url)
        for stops in parsed_url:
            if bus_stop in stops['Text'].lower():
                return stops['Value']

    # defines_get_departure which takes in a route number, direction, and stop id
    # the function then loops through a json for the first 'DepartureText'
    # this value is the time of departure
    def get_next_departure(self, route_number, direction, stop_id):
        departure_time_url = DEFAULT_URL + str(route_number) + "/" + str(direction) + "/" + str(stop_id) + JSON_FORMAT
        read_url = self.read_provided_url(departure_time_url)
        parsed_url = self.parse_provided_url(read_url)
        for times in parsed_url:
            return times['DepartureText']

    # defines a function to read a url provided
    def read_provided_url(self, provided_url):
        read_url = request.urlopen(provided_url).read().decode('utf-8')
        return read_url

    # defines a function that takes a read url and parses it
    def parse_provided_url(self, read_url):
        parsed_url = json.loads(read_url)
        return parsed_url
