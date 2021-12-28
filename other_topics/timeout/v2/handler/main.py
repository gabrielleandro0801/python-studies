import time
import timeout_decorator

TIMEOUT: int = 5


@timeout_decorator.timeout(TIMEOUT)
def func_b() -> int:
    try:
        time_to_sleep: int = 6
        print(f'\nFunction [{func_b.__name__}] has {TIMEOUT}s to run, but will sleep for {time_to_sleep} seconds')

        time.sleep(time_to_sleep)
        return 1
    except timeout_decorator.timeout_decorator.TimeoutError:
        print(f'As expected, function [{func_b.__name__}] timed out!')


if __name__ == '__main__':
    # Validating timeout using lib timeout-decorator - v2
    # A function which returns an int value and has 5s to run
    # If its time expires, it will return None due to the except clause

    func_b()
    print('\nBoth functions ran with their specific timeouts!')
