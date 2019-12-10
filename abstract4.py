from abc import *


class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass


# class bus(Vehicle):
#	def m1(self):
#		print('test')
class Bus(Vehicle):
    def noofwheels(self):
        print('test')


class Auto(Vehicle):
    def noofwheels(self):
        print('testing')


# a=Vehicle()
# a.test()
b = Bus()
b.noofwheels()
c = Auto()
c.noofwheels()


'''
output;
test
testing'''