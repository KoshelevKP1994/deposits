"""
test for main.py
"""

import unittest

from fastapi.testclient import TestClient
from main import app
from app import config


client = TestClient(app)


class TestApp(unittest.TestCase):

    def test_healthcheck(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_post_profitability_scheduler(self):
        data = {
            "date": '31.01.2021',
            "periods": 3,
            "amount": 10_000,
            "rate": 6
        }
        expect_scheduler = {'31.01.2021': 10050.0, '28.02.2021': 10100.25, '31.03.2021': 10150.75}

        response = client.post("/deposits/v1/profitability_scheduler", json=data)

        assert response.status_code == 200
        assert response.json() == expect_scheduler

    def test_validation_exception_handler(self):
        data = {
            "date": 'wrong data mock',
            "periods": 3,
            "amount": 10_000,
            "rate": 6
        }
        expected_error = "[{'type': 'value_error', 'loc': ('body', 'date'), " \
                         "'msg': \"Value error, time data 'wrong data mock' does not match format '%d.%m.%Y'\", " \
                         "'input': 'wrong data mock', 'ctx': {'error': " \
                         "ValueError(\"time data 'wrong data mock' does not match format '%d.%m.%Y'\")}}]"

        response = client.post("/deposits/v1/profitability_scheduler", json=data)

        assert response.status_code == 400
        assert response.json() == {'error': expected_error}


if __name__ == "__main__":
    unittest.main()