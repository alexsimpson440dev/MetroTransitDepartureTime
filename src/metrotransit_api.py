import urllib.request as request
import json
from datetime import datetime

# setting Constant Variables
DEFAULT_URL='http://svc.metrotransit.org/NexTrip/'
JSON_FORMAT='?format=json'

class MetroTransitAPI(object):
    def __init__(self):
        pass

    # get routes function sets a dictionary
    # then reads/parses the routes json file, gets route number and description, then returns them in a dictionary
    def get_routes(self):
        routes_dict = dict()

        routes_url = DEFAULT_URL + "Routes" + JSON_FORMAT
        read_url = self.read_provided_url(routes_url)
        parsed_url = self.parse_provided_url(read_url)
        for routes in parsed_url:
            route_number = routes['Route']
            route_name = routes['Description']

            routes_dict[route_number] = route_name
        return routes_dict

    # get directions functions gets the two directions that will work with a provided route
    def get_directions(self, route_number):
        direction_dict = dict()

        direction_url = DEFAULT_URL + "Directions/" + route_number + JSON_FORMAT
        read_url = self.read_provided_url(direction_url)
        parsed_url = self.parse_provided_url(read_url)
        for directions in parsed_url:
            value = directions['Value']
            direction = directions['Text']

            direction_dict[value] = direction
        return direction_dict


    # defines the get_stop_identifier which intakes a bus stop name, direction number, and route number
    # the function then returns the bus stop number if applicable
    def get_stop_identifier(self, direction, route_number):
        stops_dict = dict()

        stops_url = DEFAULT_URL + "Stops/" + route_number + "/" + direction + JSON_FORMAT
        read_url = self.read_provided_url(stops_url)
        parsed_url = self.parse_provided_url(read_url)
        for stops in parsed_url:
            value = stops['Value']
            text = stops['Text']

            stops_dict[value] = text
        return stops_dict

    # defines_get_departure which takes in a route number, direction, and stop id
    # the function then loops through a json for the first 'DepartureText'
    # this value is the time of departure
    def get_next_departure(self, route_number, direction, stop_id):
        departure_time_url = DEFAULT_URL + str(route_number) + "/" + str(direction) + "/" + str(stop_id) + JSON_FORMAT
        read_url = self.read_provided_url(departure_time_url)
        parsed_url = self.parse_provided_url(read_url)
        # sends the parsed url to the checking function
        check = self.check_time_actual(parsed_url)
        # if the check function returns true, then the program will return the value of Departure text
        # this is because if it is true it is giving a real time value in minutes
        if check is True:
            for times in parsed_url:
                departure_time =  times['DepartureText']
                if departure_time == "Due":
                    return departure_time
                else:
                    return departure_time + "utes"

        # if the checks returned value is not true, then it returns bool false
        # program will subtract current time from it to return correct value in minutes until departure
        else:
            for times in parsed_url:
                returned_time = times['DepartureText']
                parsed_time = datetime.strptime(returned_time, '%I:%M')
                current_time = datetime.now()

                departure_time = parsed_time - current_time
                departure_time = str(departure_time)
                days_hours,minutes,second = departure_time.split(':')
                return minutes + " Minutes"

    # defines a check function for the next departure
    # checks to see if the actual time is true
    # if APIs actual value is true, it returns a bool True
    def check_time_actual(self, parsed_url):
        for value in parsed_url:
            actual = value['Actual']
            if actual is True:
                return True
            else:
                return False

    # defines a function to read a url provided
    def read_provided_url(self, provided_url):
        read_url = request.urlopen(provided_url).read().decode('utf-8')
        return read_url

    # defines a function that takes a read url and parses it
    def parse_provided_url(self, read_url):
        parsed_url = json.loads(read_url)
        return parsed_url
