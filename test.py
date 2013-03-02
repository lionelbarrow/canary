import canary
import unittest

class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        canary.app.config['TESTING'] = True
        self.app = canary.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_forecast(self):
        response = self.app.get('/forecast')
        assert response.status_code == 200

    def test_about(self):
        response = self.app.get('/faq')
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
