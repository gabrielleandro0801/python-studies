import threading
import time
from typing import List

burgers = {}


def _make_burger(order_num):
    print(f"Preparing burger #{order_num}...")
    time.sleep(5)
    print(f"Burger made #{order_num}")

    burgers[order_num] = {"burger": order_num}


def main():
    order_queue: List[threading.Thread] = []

    for i in range(3):
        # The return value of methods that are run inside threading.Thread are misses
        # So, "_make_burger" has to set its return value into the global variable "burgers"
        task = threading.Thread(target=_make_burger, args=(i,))
        order_queue.append(task)

        # This line invokes the target method (_make_burger)
        task.start()

    for task in order_queue:
        # This line waits to the task to be finished
        task.join()


if __name__ == "__main__":
    # This version is async
    # All the burger orders are set in different threads and executed concurrently
    # The last for assures all threads will be awaited before the execution ends
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed:0.2f} seconds.")
