''' in the abstract method concept what we have in parent class  that all abstract methods should have in child class then only it will works
other wise it not works.''' 
from abc import *

class Vehicle(ABC):
	@abstractmethod
	def noofwheels(self):
		pass
	@abstractmethod	
	def test(self):
		print('this is testing')	
	def qq(self):
		print('qqqq')
		
#class bus(Vehicle):
#	def m1(self):
#		print('test')
class Bus(Vehicle):
	def noofwheels(self):
		print('test')
		super().test()
	def test(self):
		print('test11111')
	def testing(self):
		print('yes')
		
class Auto(Vehicle):
	def noofwheels(self):
		print('testing')
	def test(self):
		print('2222222')	
	def wow(self):
		print('wow')
	
#a=Vehicle()
#a.test()
b=Bus()
b.noofwheels()
b.testing()
c=Auto()
c.noofwheels()		
c.wow()
