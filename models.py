from runnable import Runnable
import time

class Car (Runnable):

    def __init__(self, wheels, doors, seats, maxSpeed):
        self.wheels = wheels
        self.doors = doors
        self.seats = seats
        self.maxSpeed = maxSpeed

    def info(self):
        print ("\n")
        print ("wheels=" + str(self.wheels))
        print ("doors=" + str(self.doors))
        print ("seats=" + str(self.seats))
        print ("maxSpeed=" + str(self.maxSpeed))

    def run(self) :
        for i in range(0, 10):
            print (self.maxSpeed)
            time.sleep(1)

    # def call(self) :
    #     self.run()