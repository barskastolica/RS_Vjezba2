"""
    Definirajte korutinu koja će simulirati dohvaćanje podataka s weba.
    Podaci neka budu lista brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde.
    Listu brojeva definirajte comprehensionom.
    Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke.
    Riješite bez korištenja asyncio.gather() i asyncio.create_task() funkcija.
"""

import asyncio
import time

async def dohvacanje():
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci dohvaceni")
    return podaci

async def main():
    rezultat = await dohvacanje()
    print(f"Podaci: {rezultat}")
    
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrime: {round(t2-t1, 2)} sek")