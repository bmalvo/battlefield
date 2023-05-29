"""The cockroach is one of the fastest insects. Write a function which takes its speed in km per
hour and returns it in cm per second, rounded down to the integer (= floored)."""
from math import floor


def cockroach_speed(km_per_h):
    """Convert speed from km/h
    to s/cm"""
    return floor(km_per_h*27.777778)
