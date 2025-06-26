## Execution Order
1. First, run the file **sync_code.py**, which contains the sync execution of the code.

## Asyncio
1. Run the file **asyncio/async_await.py**, which contains the async execution of the code.
2. Run the file **asyncio/async_await_with_max_workers.py**, which contains the async execution of the code with a max number of workers.
3. Run the file **asyncio/async_await_with_different_tasks.py**, which contains the async execution of different methods with a max number of workers.

## Threading
1. Run the file **threading/threads.py**, which contains the async execution of the code.


## Briefing
The difference between **Asyncio (async/await)** and **Threading** is who is in charge of which process in running and when.
In async/await there's the called _cooperative concurrency_, where a _coroutine_/_future_ gives up its control to another _coroutine_/_future_ to let others have a go.
In Threading is the OS who will be in curb of which process is running.

### Example
Cooperative concurrency is like a meeting with a microphone being passed around for people to speak. Whoever has the microphone can talk, and when they are done or have nothing else to say, they will pass the microphone to the next person. In contrast, multithreading is a meeting where there is a chairperson who will determine who has the floor at any given time.

#### Source
[JetBrains Blog - Faster Python: Concurrency in async/await and threading](https://blog.jetbrains.com/pycharm/2025/06/concurrency-in-async-await-and-threading/#how-does-threading-work-in-python)
