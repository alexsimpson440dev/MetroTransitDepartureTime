import unittest
from src.metrotransit_api import MetroTransitAPI
API = MetroTransitAPI()

class TestAPI(unittest.TestCase):

    # tests to see if the returned input is 901, which is equal to the route number for metro blue line.
    def test_route_number(self):
        defined_input = "metro blue line"
        defined_output = "901"
        self.assertEqual(API.get_route_number(defined_input), defined_output)


if __name__ == "__main__":
    unittest.main()