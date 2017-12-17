import unittest
from src.metrotransit_api import MetroTransitAPI
API = MetroTransitAPI()

class TestAPI(unittest.TestCase):

    # tests to see if the returned input is 901, which is equal to the route number for metro blue line.
    def test_route_number(self):
        defined_input = "metro blue line"
        defined_output = "901"
        self.assertEqual(API.get_route_number(defined_input), defined_output)

    # tests to see if returned bus stop id is correct
    def test_bus_stop_number(self):
        bus_stop_name = "mall of america station"
        direction_number = "4"
        route_number = "901"
        defined_output = "MAAM"
        self.assertEqual(API.get_stop_identifier(bus_stop_name, direction_number, route_number), defined_output)


if __name__ == "__main__":
    unittest.main()