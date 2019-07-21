# -*- coding: utf-8 -*-
from importlib.machinery import SourceFileLoader
import math

try:
    from core import verified, VerifiedData
except ModuleNotFoundError:
    core = SourceFileLoader(
        'core', 'jupyter_demo/core.py').load_module()
    from core import verified, VerifiedData

"""
Maximum number of pigs that can fit on a ship. Don't expose this as a default to the function, or
it could be troublesome to change later.
"""
MAX_LOAD = 400

PIG_WEIGHT = 70  # todo: verify the weight of each year's pigs


@verified
def get_shipping_range(load=-1) -> VerifiedData:
    """
    Determine how far a Kamarian ship can travel, when loaded with a population `load` of pigs.
    :param load: The headcount of pigs.
    :type load: int
    :return: The distance (in kilometres) that a ship can travel; as well as a message about its
        interpretation.
    :rtype: tuple(float, str)
    """
    # todo: Ask our naval architect to help us with sanity-checking this implementation. It seems
    # odd that the pigs' exhaustion is independent of the lunar cycle.
    if load < 0:
        load = MAX_LOAD
    if load > MAX_LOAD:
        raise ValueError("We cannot fit {count} pigs on the boat, according to our naval "
                         "architect.".format(count=MAX_LOAD))
    """
    Our naval architect informed us that a pig's wings have a maximum lift capacity equal to 1.4×
    its own weight; and that there was an exponential enthusiasm effect within the pigs of 1.05, to
    prolong their range.
    """
    net_mass = 50 * 10 ** 3 - (load * PIG_WEIGHT * 1.4)
    fuel_distance = 2000 - (net_mass * 0.01)
    """
    Our naval architect informed us that when the pigs are exhausted, then if the ship doesn't stop,
    they'll have a mutiny and raid the engine room to prevent the ship going any further.
    """
    exhaustion_time = 50 * math.pow(1.05, load)
    """
    Each pig adds a bit of wind resistance.
    """
    top_speed = 40 - 0.025 * load
    exhaustion_distance = top_speed * exhaustion_time
    if exhaustion_distance < fuel_distance:
        return exhaustion_distance, "{load} pigs can take us {distance} km before they become " \
                                    "exhausted and have a mutiny.".format(load=load,
                                                                          distance=exhaustion_distance)
    else:
        return fuel_distance, "{load} pigs can be taken {distance} km before we'll run out of " \
                              "fuel.".format(load=load, distance=fuel_distance)
