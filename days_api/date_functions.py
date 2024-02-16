"""Functions for working with dates."""

from datetime import datetime


def convert_to_datetime(date: str) -> datetime:
    '''Converts a date string in the format dd.mm.yyyy to a datetime object'''
    try:
        d = datetime.strptime(date, "%d.%m.%Y")
        return d

    except:
        raise ValueError('Unable to convert value to datetime.')


def get_days_between(first: datetime, last: datetime) -> int:
    '''Gets the amount of days between two dates'''
    if isinstance(first, datetime) and isinstance(last, datetime):

        difference = last - first

        return difference.days

    raise TypeError('Datetimes required.')


def get_day_of_week_on(date: datetime) -> str:
    '''Gets the day of the week that a certain date lands on'''
    if not isinstance(date, datetime):
        raise TypeError('Datetime required.')

    return datetime.strftime(date, '%A')
