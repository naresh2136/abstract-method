from abc import *


class Test(ABC):
    pass


t = Test()
'here we can create object'
'in the class we add(ABC)even it create object why because of class doesnt have abstract method '


class Test:
    @abstractmethod
    def m1(self):
        print('this 1')
        pass


a = Test()
a.m1()
'output: this'
'here we can create object'
'why because of we dont add (ABC)in the class'

# class Test(ABC):
#	@abstractmethod
#	def m1(self):
#		print('this ')
#		pass

a = Test()
a.m1()
'output: Error cant instantiate abstract class Test with abstract methods m1 '
'here we cont create object'
'why becouse of in the class we add(ABC) and we have abstract method also'


class Test(ABC):
    @abstractmethod
    def m1(self):
        print('this 2')
        pass

    def m2(self):
        print('this is testing')


a = Test()
# a.m1()
a.m2()