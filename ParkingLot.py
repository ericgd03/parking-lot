from Car import Car
from Ticket import Ticket

class ParkingaLot:

    def __init__(self, spacesAvaileble):

        self.spacesAvailable = spacesAvaileble

    def enter(self, car: Car):

        if (self.spacesAvailable > 0):

            newTicket = Ticket(car.plate)

            self.spacesAvailable -= 1

            print("entraste")

            return newTicket
        
        return None



