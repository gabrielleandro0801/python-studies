class ClassA:
    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print(f'My name is [{self.__name}]')


class ClassB:
    def __init__(self, age):
        self.__age = age

    def print_age(self):
        print(f'I am [{self.__age}] years old')


def factory():
    return lambda: ClassA('Gabriel'), lambda: ClassB(20)


if __name__ == '__main__':
    # Factory - v1
    # Creating a function that returns a tuple of lambda functions

    factory = factory()
    a = factory[0]()
    b = factory[1]()

    a.print_name()
    b.print_age()
