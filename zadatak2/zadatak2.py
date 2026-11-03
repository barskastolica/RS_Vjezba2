"""
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba.
Prva korutina neka vrati listu proizvoljnih rječnika
(npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde,
a druga korutina neka vrati listu proizvoljnih rječnika
(npr. koji reprezentiraju podatke o proizvodima) nakon 5 sekundi.
Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate.
Program se mora izvršavati ~5 sekundi.
"""
import asyncio
import time

async def dohvati_korisnike():
    await asyncio.sleep(3)
    return [
        {"id":1, "ime": "Bare"},
        {"id":2, "ime": "Mate"},
        {"id":3, "ime": "Petar"}
    ]

async def dohvati_proizvode():
    await asyncio.sleep(5)
    return [
        {"id":101, "naziv":"Pegla", "cijena":15},
        {"id":102, "naziv":"Lopata", "cijena":5},
        {"id":103, "naziv":"Cipele", "cijena":20}
    ]

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvati_korisnike(),
        dohvati_proizvode()
    )
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrime: {round(t2-t1, 2)} sek")