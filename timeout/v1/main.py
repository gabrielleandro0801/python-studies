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


if __name__ == '__main__':
    # Validating timeout using lib timeout-decorator - v1
    # A void function which contains 5s to run

    func_a()
    print(f'\nFunction {func_a.__name__} ran with their specific timeout!')
