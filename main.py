
from ParkingLot import ParkingaLot
from Car import Car

myParkingLot = ParkingaLot(20)

myCar = Car("1234")

myParkingLot.enter(myCar)

print(myParkingLot.spacesAvailable)