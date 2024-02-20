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

    def __init__(self, start):
        """Creates Serial Generator beginning at start"""
        self.start = start
        self.count = start

    def __repr__(self):
        return f"""Serial Generator with start of {self.start}
            and current count of {self.count}"""

    def reset(self):
        """Sets count back to original start value"""
        self.count = self.start

    def generate(self):
        """Increments count by 1 and returns the new count value."""
        self.count += 1
        return self.count - 1
#TODO: count can be called next_value or similar to be clearer