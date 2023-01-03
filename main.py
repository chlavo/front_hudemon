import asyncio
import data
from datetime import datetime
import pandas as pd

async def main():
    print(f"It's now {data.chromaticka_tabulka(0)}")

    print('Hello, World! 123')
    print(f"It's now {datetime.now()}")
    async def foo():
        df = pd.DataFrame({
                "name":["karel", "ondrej"],
                "vek":[45, 68]
                })
        while True:
            output = datetime.now()
            pyscript.write("myNum", output)
            output1 = Element("myNum1")
            output1.write(datetime.now())
            await asyncio.sleep(1)
            
            output3 = Element("myPandas")
            output3.write(df.head())
    await foo()

#asaaas
        
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())