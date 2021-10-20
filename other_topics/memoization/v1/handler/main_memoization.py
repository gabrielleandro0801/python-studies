def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            print(f'== Value for parameter [{x}] not in cache, setting now ==')
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
    for number in range(10, -1, -1):
        fib_my_number = fib(number)
        print(f'Fibonacci of {number}: [{fib_my_number}], executing fib() and caching values if not exists')
