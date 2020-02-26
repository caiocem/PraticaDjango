import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def isYYYYMMDD(value):
    """
    Let's validate the date
    """
    try:
        datetime.datetime.strptime(value, '%Y/%m/%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY/MM/DD")
