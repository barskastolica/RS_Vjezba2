"""
Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine fetch_data(2)
bez da ju awaitate unutar main funkcije?
Preciznije, dokažite kako se može ispisati tekst Dovršio sam s 2. unutar korutine fetch_data(2)
bez da eksplicitno pozivate await task2 unutar main() funkcije.
"""
#zadatak kopiran iz skripte
import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

"""
u main() smo definirali dva taska, a pokretanjem main() automatski se pokrece i event loop koji ce 
odraditi oba definirana taska njjihovim redoslijedom
Event loop ce zapoceti oba taska, a dobit cemo ispis "Dovrsio sam s 1" i rezultat za task1, a ne za task2 zato
sto task1 traje krace (1 sek) od task2 (2 sek)
Nakon izvrsenja task1 event loop se zatvara zato sto je radia samo 1 sek i nije se stigao odraditi task2
Ako "natjeramo" main() da ostane "otvoren" jos malo sa sleep odradit ce se task2 i ispisat "Dovrsio sam s 2"
"""
async def main():
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) #schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    await asyncio.sleep(1) #dodali smo sleep 1 sekundu kako bi event loop ostao "otvoren" dok se ne odradi task2
    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")