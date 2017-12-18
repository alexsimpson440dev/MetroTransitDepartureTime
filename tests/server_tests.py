from app import app
import unittest

# tests server
class ServerTest(unittest.TestCase):

    # test to check the response code
    def test_index(self):
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # tests to see if main page is loading
    def test_index_loads(self):
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Welcome' in response.data)

    # tests to see if Minutes or Due is in the page when loading with given values
    def test_index_time(self):
        tester = app.test_client()
        response = tester.get('/time?stop=MAAM&route=901&direction=4', content_type='html/text')
        self.assertTrue(b'Minutes' or b'Due' in response.data)

if __name__ == "__main__":
    unittest.main()