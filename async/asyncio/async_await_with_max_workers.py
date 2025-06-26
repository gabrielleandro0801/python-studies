import asyncio
import time
from asyncio import Queue

order_queue: Queue = asyncio.Queue()


def add_orders_into_queue():
    for i in range(3):
        order_queue.put_nowait(_make_burger(i))


async def _make_burger(order_num):
    print(f"Preparing burger #{order_num}...")
    await asyncio.sleep(5)
    print(f"Burger made #{order_num}")

    return {"burger": order_num}


class Staff:
    def __init__(self, name: str):
        self.__name = name

    async def working(self):
        while order_queue.qsize() > 0:
            print(f"{self.__name} is working...")
            task = await order_queue.get()
            await task
            print(f"{self.__name} finished a task...")


async def main():
    staff1 = Staff("John")
    staff2 = Staff("Mark")

    add_orders_into_queue()

    await asyncio.gather(staff1.working(), staff2.working())


if __name__ == "__main__":
    # In this case, there's a queue of async operations to be performed
    # There are only two available workers, John and Mark, to execute them
    # So, on the method "working", they access the same queue to retrieve the operations
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed:0.2f} seconds.")
