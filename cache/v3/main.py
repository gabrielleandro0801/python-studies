from cachetools import cached, TTLCache

SECONDS_TTL_CACHE: int = 100
INVALID_NUMBER: int = 3


@cached(TTLCache(maxsize=1024, ttl=SECONDS_TTL_CACHE))
def to_square(number):
    if number == INVALID_NUMBER:
        raise Exception(f'\nNumber invalid: [{number}], this execution will not cache\n')
    return number ** 2


if __name__ == '__main__':
    # Cache using lib cachetools - v3
    # Caching values in a simple dict which maxsize is 1024 and the TTL of cache is 10s
    # The difference for v2 is that now this function raises an Exception
    # When the exception is raised, no value is cached

    for i in range(0, 3):
        print(f'{i} ** 2 = {to_square(i)}')

    print('\n')
    for i in range(0, 7):
        try:
            print(f'{i} ** 2 = {to_square(i)}')
        except Exception as e:
            print(e)
