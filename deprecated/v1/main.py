from deprecated import deprecated


@deprecated
def function_one(message):
    print("[function_one] Hello, %s" % message)


@deprecated("This function is rotten, use 'function_three' instead")
def function_two(message):
    print("[function_two] Hello, {}" .format(message))


@deprecated(version='0.0.3', reason="deprecated function")
def function_three(message):
    print(f"[function_three] Hello, {message}")


@deprecated(reason="do not call it", action="error")
def function_four(message):
    print(f"[function_four] Hi, {message}")


@deprecated(reason="do not call it", action="ignore")
def function_five(message):
    print(f"[function_five] Hi, {message}")


@deprecated("This class is deprecated")
class MyClass:
    def __init__(self):
        print(f"[Constructor of {MyClass.__name__}] called")


if __name__ == '__main__':
    # Deprecated - v1
    # Tagging functions and classes as deprecated, even throwing exceptions if needed
    name = 'Gabriel'

    # Functions
    function_one(name)
    function_two(name)
    function_three(name)

    try:
        function_four(name)
    except DeprecationWarning as e:
        print('[function_four] threw an exception')

    function_five(name)

    # Classes
    my_class = MyClass()
