import asyncio
import time
import random


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return random.randint(0,10)

async def nested():
    print ("aaa")
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested()) # tas is awaitable

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    x = await task
    print (x)

    # running coroutines in parallel (it takes 2 secs not 3)
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))
        task2 = tg.create_task(
            say_after(2, 'world'))
        print(f"started at {time.strftime('%X')}")

    print (task1.result(), task2.result())

    # The await is implicit when the context manager exits.
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())