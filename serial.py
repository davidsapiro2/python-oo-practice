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
        self.count = -1

    def __repr__(self):
        return f"""Serial Generator with start of {self.start}
            and current count of {self.start + self.count}"""

    def reset(self):
        """Sets count back to original start value"""
        self.count = -1

    def generate(self):
        """Increments count by 1 and returns the new count value."""
        self.count += 1
        return self.count + self.start
