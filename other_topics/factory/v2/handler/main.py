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
    return {
        'generateClassA': lambda: ClassA('Gabriel'),
        'generateClassB': lambda: ClassB(20)
    }


if __name__ == '__main__':
    # Factory - v2
    # Creating a function that returns a dict of lambda functions
    factory = factory()

    a = factory.get('generateClassA')()
    b = factory.get('generateClassB')()

    a.print_name()
    b.print_age()
