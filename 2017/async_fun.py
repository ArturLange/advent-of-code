import asyncio


async def hello1():
    wait_time = 0
    while True:
        print(f'Task 1, second {wait_time}')
        await asyncio.sleep(1)
        wait_time += 1


async def hello2():
    wait_time = 0.
    while True:
        print(f'Task 2, second {wait_time:.3}')
        await asyncio.sleep(1.3)
        wait_time += 1.3


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(
            hello1(),
            hello2()
        )
    )
    loop.close()
