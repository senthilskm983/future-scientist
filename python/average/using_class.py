import functools
import operator


class Sample:
    """
    sample method
    """

    def __init__(self, values):
        """
        Constructor call
        """
        self.values = values

    def average(self):
        """
        calculate average
        """
        _sum = functools.reduce(operator.add, self.values)
        return _sum / len(self.values)