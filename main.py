import asyncio
import data
from datetime import datetime


async def main():
    print(f"It's now {data.chromaticka_tabulka(0)}")

    print('Hello, World! 123')
    print(f"It's now {datetime.now()}")
    async def foo():
        while True:
            output = datetime.now()
            pyscript.write("myNum", output)
            output1 = Element("myNum1")
            output1.write(datetime.now())
            await asyncio.sleep(1)
    await foo()

#asaaas
        
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())