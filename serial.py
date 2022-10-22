"""Python serial number generator."""



class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # this variable tracks how many times we have called the generate method
    count = 0

    def __init__(self, start):
        self.start = start
    
    def generate(self):
        """returns the next incremental number from the starting number"""
        num = self.start
        self.start += 1
        self.count += 1
        return num

    def reset(self):
        """resets the generator back to the starting number"""
        self.start = self.start - self.count