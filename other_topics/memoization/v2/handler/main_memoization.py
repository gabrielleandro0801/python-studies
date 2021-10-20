from other_topics.memoization.v2.utils.memoize import Memoize


@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)


@Memoize
def to_square(n, s):
    return n**s


if __name__ == '__main__':
    for number in range(0, 11):
        fib_my_number = fib(number)
        square_my_number = to_square(number, number)

        print(f'Fibonacci of {number}: [{fib_my_number}], executing fib() and caching values if not exists')
        print(f'{number} square {number}: [{square_my_number}], executing to_square() and caching values if not exists\n')
