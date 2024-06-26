"""
schemas for deposits
"""

import datetime

from pydantic import BaseModel, field_validator
from pydantic.types import conint, confloat

from app import config


class Deposit(BaseModel):
    """
    deposit input schema
    """
    date: datetime.date
    periods: conint(ge=config.MIN_PERIOD, le=config.MAX_PERIOD)
    amount: conint(ge=config.MIN_AMOUNT, le=config.MAX_AMOUNT)
    rate: confloat(ge=config.MIN_RATE, le=config.MAX_RATE)

    @field_validator("date", mode="before")
    def str_to_date(cls, v: str) -> datetime.date:
        """
        Extract the date from a string like '20-12-2004'.
        """
        return datetime.datetime.strptime(v, '%d.%m.%Y').date()
