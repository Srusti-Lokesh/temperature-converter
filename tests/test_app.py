import unittest
from app import app, convert_temperature


class TemperatureConverterTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert_temperature(0, "C", "F"), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert_temperature(212, "F", "C"), 100)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert_temperature(0, "C", "K"), 273.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert_temperature(273.15, "K", "C"), 0)

    def test_absolute_zero_validation(self):
        with self.assertRaises(ValueError):
            convert_temperature(-274, "C", "K")

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        response = self.client.get("/api/convert?value=100&from=C&to=F")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 212.0)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
