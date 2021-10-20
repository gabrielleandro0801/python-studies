def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    my_number = 5
    fib_my_number = fib(my_number)
    print(f'Fibonacci of {my_number}: [{fib_my_number}], caching values internally')

    my_number = 3
    fib_my_number = fib(fib_my_number)
    print(f'Fibonacci of {my_number}: [{fib_my_number}], obtained from internal cache')

    my_number = 7
    fib_my_number = fib(fib_my_number)
    print(f'Fibonacci of {my_number}: [{fib_my_number}], not in cache, executing function fib()')
