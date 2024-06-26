"""
api for working with deposits
"""

import calendar

from app.schema import Deposit


def calculate_deposit_profitability_scheduler(deposit: Deposit) -> dict:
    scheduler = {}

    amount = deposit.amount

    year = deposit.date.year
    month = deposit.date.month

    for _ in range(deposit.periods):
        day = calendar.monthrange(year, month)[1]
        if month >= 10:
            date_str = f"{day}.{month}.{year}"
        else:
            date_str = f"{day}.0{month}.{year}"

        amount += amount * deposit.rate / 100 / 12

        scheduler[date_str] = round(amount, 2)

        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

    return scheduler
