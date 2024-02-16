"""Functions for working with dates."""

from datetime import datetime


def convert_to_datetime(date: str) -> datetime:
    try:
        d = datetime.strptime(date, "%d.%m.%Y")
        return d

    except:
        raise ValueError('Unable to convert value to datetime.')


def get_days_between(first: datetime, last: datetime) -> int:
    if isinstance(first, datetime) and isinstance(last, datetime):

        difference = last - first

        return difference.days

    raise TypeError('Datetimes required.')


def get_day_of_week_on(date: datetime) -> str:
    if not isinstance(date, datetime):
        raise TypeError('Datetime required.')
    else:
        return datetime.strftime(date, '%A')
