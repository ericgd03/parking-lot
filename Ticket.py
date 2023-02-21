import datetime

class Ticket:

    def __init__(self, carPlate):

        self.carPlate = carPlate

        ticketDate = datetime.datetime.now()

        self.number = self.__generateUniqueNumberBasedOnDate(ticketDate)

    def __generateUniqueNumberBasedOnDate(date, time):

        return str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second)

