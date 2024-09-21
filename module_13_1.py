import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    k = 20 / int(power)
    balls = 5
    for i in range(1, balls+1):
        await asyncio.sleep(k)
        print(f'Силач {name} поднял {i}.')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

print('+++Турнир завершен!!!+++')



