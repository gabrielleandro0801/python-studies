import time
from cachetools import cached, TTLCache


SECONDS_TTL_CACHE: int = 10


@cached(TTLCache(maxsize=1024, ttl=SECONDS_TTL_CACHE))
def fib(n):
    print(f'Executing [{fib.__name__}] for [{n}]')
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # Cache using lib cachetools - v2
    # Caching values in a simple dict which maxsize is 1024 and the TTL of cache is 10s

    print(f'Executing for the first time and caching it locally for {SECONDS_TTL_CACHE}s')
    print(f'Fibonacci de 10: [{fib(10)}]')

    print('\nExecuting for the second time and adding three more numbers, the rest are in cache')
    print(f'Fibonacci de 13: [{fib(13)}]')

    print(f'\nSleeping for {SECONDS_TTL_CACHE}s')
    time.sleep(SECONDS_TTL_CACHE)

    print('\nExecuting for the third time, now the values are not in cache anymore')
    print(f'Fibonacci de 13: [{fib(13)}]')

    print('\nExecuting for the fourth time, and the values are in cache again')
    print(f'Fibonacci de 7: [{fib(7)}]')
