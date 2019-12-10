from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print('i can walk and run..')


class Snake(Animal):
    def move(self):
        print('i can crawl..')


def main():
    #	a1=Animal()
    h1 = Human()
    h1.move()

    s1 = Snake()
    s1.move()


if __name__ == '__main__':
    main()

'''output=
i can walk and run..
i can crawl..'''
