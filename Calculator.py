class Calculator:
    def __init__(self, initial, rate):
        self._initial = initial
        self._rate = rate/100

    def total_interest(self, time):
        return self._initial * self._rate * time

    def time_required(self, total):
        return total/(self._initial * self._rate)
