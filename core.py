# -*- coding: utf-8 -*-
from datetime import datetime
from functools import wraps

import pytz


class VerifiedData(object):
    """
    This class embeds data with metadata about its provenance, for extra confidence.
    """
    def __init__(self, data, calculation_time=None, calculation_log=None, *args, **kwargs):
        self.data = data
        self.calculation_time = calculation_time or datetime.now(tz=pytz.UTC)
        self.calculation_log = calculation_log or 'Magically calculated by infallible comrade 🔮✨.'
        
    def __str__(self):
        return "{time}: {log}\t {data}".format(time=self.calculation_time,
                                               log=self.calculation_log, data=str(self.data))


def verified(naïve_function):
    """
    Revise a function to return verified data, rather than raw data
    :param naïve_function: A function which is to be transformed into the verified form.
    :return: A revised function
    """
    @wraps(naïve_function)
    def verified_function(*args, **kwargs):
        # todo: embed the return type in the wrapper rather than each function using it
        calculation_time = datetime.now(tz=pytz.UTC)
        data, message = naïve_function(*args, **kwargs)
        verified_data = VerifiedData(data, calculation_time=calculation_time,
                                     calculation_log=message)
        return verified_data
    return verified_function
