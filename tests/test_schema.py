"""
test for schema.py
"""

import unittest
import datetime
from app.schema import Deposit
from app import config
from pydantic import ValidationError


class TestDepositDateParser(unittest.TestCase):
    data = {
        "date": '11.01.2021',
        "periods": config.MIN_PERIOD,
        "amount": config.MIN_AMOUNT,
        "rate": config.MIN_RATE
    }

    deposit = Deposit(**data)

    assert deposit.date == datetime.date(2021, 1, 11)


class TestDepositDataLimits(unittest.TestCase):

    def test_min_period(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MIN_PERIOD - 1,
            "amount": config.MIN_AMOUNT,
            "rate": config.MIN_RATE
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True

    def test_max_period(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MAX_PERIOD + 1,
            "amount": config.MIN_AMOUNT,
            "rate": config.MIN_RATE
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True

    def test_min_amount(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MIN_PERIOD,
            "amount": config.MIN_AMOUNT - 1,
            "rate": config.MIN_RATE
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True

    def test_max_amount(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MIN_PERIOD,
            "amount": config.MAX_AMOUNT + 1,
            "rate": config.MIN_RATE
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True

    def test_min_rate(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MIN_PERIOD,
            "amount": config.MIN_AMOUNT,
            "rate": config.MIN_RATE - 1
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True

    def test_max_rate(self):
        data = {
            "date": '11.01.2021',
            "periods": config.MIN_PERIOD,
            "amount": config.MIN_AMOUNT,
            "rate": config.MAX_RATE + 1
        }

        try:
            Deposit(**data)
            raise ValueError("data limit broken")
        except ValidationError:
            assert True


if __name__ == "__main__":
    unittest.main()
