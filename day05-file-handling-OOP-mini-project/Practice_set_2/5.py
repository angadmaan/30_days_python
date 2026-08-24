# Create a class Train with methods to book a ticket, get the status of the train (number of available seats), get the fare information.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, passenger):
        print(f"Ticket booked for {passenger} on train {self.trainNo}")

    def getStatus(self):
        print(f"Train {self.trainNo} has {randint(1, 200)} seats available")

    def getFare(self, fro, to):
        print(f"Fare for train {self.trainNo} from {fro} to {to} is Rs.{randint(200, 3000)}.")


train = Train(16512)

train.book("Angad")
train.getStatus()
train.getFare("Delhi", "Amritsar")