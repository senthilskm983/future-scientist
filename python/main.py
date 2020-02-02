"""
This is the main / starting script
"""
from average import using_function, using_class

if __name__ == "__main__":
    # using functional way
    print("This is using functional way:", using_function.average([10,30,20]))
    # using OOPS way
    obj = using_class.Sample([10,30,20])
    print("This is using OOPS:", obj.average())