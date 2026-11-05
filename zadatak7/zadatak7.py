"""
Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i dovršavaju korutine
te koja su njihova stanja u različitim fazama izvođenja) na sljedećem primjeru:
"""
import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main()) 

"""
asyncio.run(main()) starta event loop i main loop 
u main() se stvaraju taskovi(Timer 1, Timer2, Timer3, svaki sa svojim trajanjem, taskovi cekaju izvodenje)
kada main() dode do await asyncio.gather(*timers) event loop prebacuje u funkciju timer() gdje se taskovi pocinju
izvrsavati redom kojim su stvoreni.
Prvo krece Timer 1 sa ispisom "Timer 1: 3 sekundi preostalo" ,a nakon toga se poziva await asyncio.sleep(1) gdje
se task Timer 1 pauzira i event loop krece na Timer 2 s ispisom "Timer 2: 5 sekundi preostalo" i nakon toga opet
await asyncio.sleep(1)-Timer 2 se pauzira i event loop prebacuje na Timer 3.
Svakim pozivanjem await asyncio.sleep(1) event loop pauzira trenutni Timer i prebacuje na iduci koji je u cekanju.
Nakon sto u Timeru isteknu sekunde dobivamo ispis "Vrijeme isteklo" za odredeni Timer i on je gotov s izvrsavanjem,
ali drugi Timeri se nastavljaju "vrtiti" dok im ne isteknu sekunde.
"""