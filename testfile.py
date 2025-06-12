import unittest

from pecan import response

from app import app

class Test_FlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_main_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        self.assertIn("Flask app is working fine" , response.get_json()['message'])

    def test_phones_page(self):
        response = self.client.get("/phones")
        self.assertEqual(response.status_code,200)
        self.assertIn("success",response.get_json()["status"])

    def test_phones_by_id_page(self):
        response = self.client.get("/phones/8973252")
        self.assertEqual(response.status_code,200)
        self.assertIn("success",response.get_json()["status"])



if __name__ == '__main__':
    unittest.main()
