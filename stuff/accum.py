# Class Accumulator

class Accumulator:

    def __init__(self):
        self._count = 0  # _count is private because is prefix with a single underscore

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more
