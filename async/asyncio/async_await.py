import asyncio
import time
from typing import Coroutine, Any, List


async def _make_burger(order_num: int):
    print(f"Preparing burger #{order_num}...")
    await asyncio.sleep(5)
    print(f"Burger made #{order_num}")

    return {"burger": order_num}


async def main():
    order_queue: List[Coroutine[Any, Any, dict[str, int]]] = []

    for i in range(3):
        order_queue.append(_make_burger(i))

    burgers: List[dict[str, int]] = await asyncio.gather(*order_queue)
    print(burgers)


if __name__ == "__main__":
    # This version is async
    # All the burger orders are set in a queue and executed concurrently
    # As each coroutine reaches its "pause" moment, the next coroutine starts
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed:0.2f} seconds.")
