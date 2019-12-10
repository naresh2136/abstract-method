'abstract method for we should import from abc import *,after that we should add the (ABC) in class level,
after that we should have @abstractmethod,after that we create amethod that should be with pass,and we can create another methods also,
if have the @abstract method and add (ABC)in class then only we cont create  an object ,other vise if we doesnt  add(ABC) in class level we create object
,if we use inhetitece inthat we should use that abstract method then only that class weworks ,otherwise if we not crest abstract  method in child class
that class will not works.the are main conditions for runthe abstract method classes'
from abc import *
class Vehicle(ABC):
	@abstractmethod
	def noofwheels(self):
		pass
	def test(self):
		print('this is testing')	
	
		
#class bus(Vehicle):
#	def m1(self):
#		print('test')
class Bus(Vehicle):
	def noofwheels(self):
		print('test')
		super().test()
	def testing(self):
		print('yes')
		
class Auto(Vehicle):
	def noofwheels(self):
		print('testing')
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


'''output:
test
this is testing
yes 
testing
wow'''
