import time
import timeout_decorator


TIMEOUT: int = 5


@timeout_decorator.timeout(TIMEOUT)
def func_a() -> None:
    try:
        print(f"Function [{func_a.__name__}] has {TIMEOUT}s to run")
        for i in range(1, 4):
            time.sleep(1)
            print(f"{i}s have passed")

        print(f'Function [{func_a.__name__}] did not time out!')
    except timeout_decorator.timeout_decorator.TimeoutError:
        print(f'Function [{func_a.__name__}] timed out!')


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
    func_a()
    b = func_b()
    print('\nBoth functions ran with their specific timeouts!')
