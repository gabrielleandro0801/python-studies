from design_patterns.singleton.v1.infrastucture.redis.redis_connection import Cache

KEY = 'my_key'
VALUE = 'value_to_cache'
TIME = 100

SCHEMA = 'redis://'
HOST = ''
PORT = '6379'
URL_CONNECTION = f'{SCHEMA}{HOST}:{PORT}'


def main():
    print(f'Instantiating first object')
    first_cache_instance = Cache.get_instance(connection=URL_CONNECTION)

    first_cache_instance.set(key=KEY, value=VALUE, time=TIME)
    response: str or None = first_cache_instance.get(key=KEY)
    print(f'Response from redis: [{response}]')

    print(f'Trying to instantiate second object')
    second_cache_instance = Cache.get_instance(connection=URL_CONNECTION)

    if first_cache_instance is second_cache_instance:
        print("Yes, both instances are the same!")


if __name__ == "__main__":
    # Singleton - v1
    # Using a single redis connection in the program not to instantiate many connections
    main()
