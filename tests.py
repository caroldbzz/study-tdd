import unittest
from app import my_web_app

class TestHome(unittest.TestCase):

    def test_get(self):
        app = my_web_app.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertIn('text/html', response.content_type)

if __name__ == '__main__':
    unittest.main()
