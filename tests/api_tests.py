import unittest
from src.metrotransit_api import MetroTransitAPI
API = MetroTransitAPI()

class TestAPI(unittest.TestCase):

    # tests to see if known values are in the returned string
    def test_displayed_time(self):
        bus_stop_id = "MAAM"
        direction_number = "4"
        route_number = "901"
        time = API.get_next_departure(route_number, direction_number, bus_stop_id)
        print(time)
        self.assertTrue('Minutes' or 'Due' in time)


if __name__ == "__main__":
    unittest.main()