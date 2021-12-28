from cachetools import cached


@cached(cache={})
def fib(n):
    print(f'Executing [{fib.__name__}] for [{n}]')
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # Cache using lib cachetools - v1
    # Caching values in a simple dict

    print('The first execution will call the function for each number.')
    first = fib(7)

    print('\nThis second one will just retrieve the data from cache..')
    second = fib(6)

    print('\nThis third one will retrieve some returns from cache but will execute the function for the last ones.')
    third = fib(9)
