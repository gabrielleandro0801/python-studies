from memoization.v1.utils.memoize import memoize


@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # Memoization - v1
    # Creating a decorator function to cache locally the input/output of a function

    for number in range(10, -1, -1):
        fib_my_number = fib(number)
        print(f'Fibonacci of {number}: [{fib_my_number}], executing fib() and caching values if not exists\n')
