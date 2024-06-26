"""
test for calculation.py
"""

import datetime
import unittest

from app.calculation import calculate_deposit_profitability_scheduler
from app.schema import Deposit


class TestCalculateDepositProfitabilityScheduler(unittest.TestCase):

    def test_with_deposit(self):
        data = {
            "date": '31.01.2021',
            "periods": 3,
            "amount": 10_000,
            "rate": 6
        }
        deposit = Deposit(**data)
        expect_scheduler = {'31.01.2021': 10050.0, '28.02.2021': 10100.25, '31.03.2021': 10150.75}

        scheduler = calculate_deposit_profitability_scheduler(deposit)

        assert scheduler == expect_scheduler

    def test_with_empty_deposit(self):
        class MockDeposit:
            date = datetime.date(2021, 1, 1)
            periods = 0
            amount = 0
            rate = 0

        deposit = MockDeposit()
        expect_scheduler = {}

        scheduler = calculate_deposit_profitability_scheduler(deposit)

        assert scheduler == expect_scheduler


if __name__ == "__main__":
    unittest.main()
