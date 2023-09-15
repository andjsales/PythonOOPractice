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

    def __init__(self, start=100):
        self.start = start
        self.counter = start

    def generate(self):
        serial = self.counter
        self.counter += 1
        return serial

    def reset(self):
        self.counter = self.start

serial = SerialGenerator(start=100)
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102
serial.reset()
print(serial.generate())  # Output: 100