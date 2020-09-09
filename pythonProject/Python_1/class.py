
class Flight(object):
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passengers)

_flight = Flight(1)
print(_flight.add_passenger('Seymur'))

