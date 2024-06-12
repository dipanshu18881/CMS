import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_process_json(self):
        response = self.client.post('/api/process-json', json={"key": "value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"key": "Value"})

if __name__ == '__main__':
    unittest.main()
