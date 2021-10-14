from singleton.infrastucture.cache.cache import Cache


if __name__ == "__main__":
    url_connection = ""
    first_cache_instance = Cache.get_instance(connection=url_connection)

    key = 'my_key'
    value = 'value_to_cache'
    time = 100

    print(f'Caching value...')
    first_cache_instance.set(key=key, value=value, time=time)

    print('Getting from cache...')
    response: str or None = first_cache_instance.get(key=key)
    print(f'Response from cache: [{response}]')

    second_cache_instance = Cache.get_instance(connection=url_connection)

    if first_cache_instance == second_cache_instance:
        print("Yes, both instances are the same!")
