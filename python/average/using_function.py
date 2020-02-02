import functools
import operator


def average(values):
    """
    calculate average
    """
    _sum = functools.reduce(operator.add, values)
    return _sum / len(values)