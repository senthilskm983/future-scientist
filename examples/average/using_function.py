import functools
import operator


def average(values):
    """
    calculate average
    """
    try:
        _sum = functools.reduce(operator.add, values)
        return _sum / len(values)
    except Exception:
        return False

def average_normal_way(values):
    """
    calculate average
    """
    _sum = 0
    for i in values:
        _sum = _sum + i
    return _sum / len(values)
