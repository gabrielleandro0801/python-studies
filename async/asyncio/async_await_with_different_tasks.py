import asyncio
import time
from asyncio import Queue

task_queue: Queue = asyncio.Queue()
order_num = 0


async def take_order():
    global order_num

    order_num += 1
    print(f"Order burger and fries for order #{order_num:04d}:")

    burger_num = await asyncio.to_thread(input, "Number of burgers:")
    for i in range(int(burger_num)):
        await task_queue.put(_make_burger(f"{order_num:04d}-burger{i:02d}"))

    fries_num = await asyncio.to_thread(input, "Number of fries:")
    for i in range(int(fries_num)):
        await task_queue.put(_make_fries(f"{order_num:04d}-fries{i:02d}"))

    print(f"Order #{order_num:04d} queued.")
    await task_queue.put(take_order())


async def _make_burger(burger_num):
    print(f"Preparing burger #{burger_num}...")
    await asyncio.sleep(5)
    print(f"Burger made #{burger_num}")

    return {"burger": burger_num}


async def _make_fries(fries_num):
    print(f"Preparing fries #{fries_num}...")
    await asyncio.sleep(2)
    print(f"Fries made #{fries_num}")

    return {"fries": fries_num}


class Staff:
    def __init__(self, name: str):
        self.__name = name

    async def working(self):
        while True:
            if task_queue.qsize() > 0:
                print(f"{self.__name} is working...")
                task = await task_queue.get()
                await task
                print(f"{self.__name} finish task...")
            else:
                # If there are no tasks to be performed, the staff member rests
                await asyncio.sleep(1)


async def main():
    task_queue.put_nowait(take_order())

    staff1 = Staff(name="John")
    staff2 = Staff(name="Jane")

    await asyncio.gather(staff1.working(), staff2.working())


if __name__ == "__main__":
    # In this case, there's a queue of different async operations to be performed
    # There are only two available workers, John and Mark, to execute them
    # So, on the method "working", they access the same queue to retrieve the operations
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed:0.2f} seconds.")
