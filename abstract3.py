from abc import *


class Test(ABC):
    def m2(self):
        print(' test2 ')

    @abstractmethod
    def m1(self):
        print('tis is test')


t = Test()
t.m1()
t.m2()
'here we can not  create object'
'why because of we have abstract method'
