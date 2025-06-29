import time
import asyncio
import requests



async def function1():
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYbn8ri6OSNfLhlNoZ8c0jbCH_qKhHPvU_MA&s"
    response = requests.get(URL)
    open ("instagram1.jpg","wb").write(response.content)
    print("func 1")

async def function2():
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAHfaKwTLBweZYHGcXLKiK1WMd_bhs-SD_jg&s"
    response = requests.get(URL)
    open ("instagram2.jpg","wb").write(response.content)
    print("func 2")

async def function3():
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2JFyVMUGB2hCmAhFXOdCydqzgsCHd2BAzEA&s"
    response = requests.get(URL)
    open ("instagram3.jpg","wb").write(response.content)
    print("nigga")

async def main():

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()


asyncio.run(main())