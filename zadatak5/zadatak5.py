"""
Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka.
Kako se u praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati
enkripciju podataka u trajanju od 3 sekunde.
Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od
ključeva prezime, broj_kartice i CVV.
Definirajte listu s 3 rječnika osjetljivih podataka.
Pohranite u listu zadaci kao u prethodnom zadatku te pozovite zadatke koristeći asyncio.gather().
Korutina secure_data mora za svaki rječnik vratiti novi rječnik u obliku:
{'prezime': 'prezime', 'broj_kartice': 'enkriptirano', 'CVV': 'enkriptirano'}.
Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash vrijednost
ulaznog stringa ili nešto slično.
"""
import asyncio
import time

async def secure_data(osjetljivi_podaci):
    await asyncio.sleep(3)
    return {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice':hash(str(osjetljivi_podaci['broj_kartice'])),
        'CVV':hash(str(osjetljivi_podaci['CVV']))
    }

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Baric', 'broj_kartice': '123456789', 'CVV': '123'},
        {'prezime': 'Anic', 'broj_kartice': '987654321', 'CVV': '321'},
        {'prezime': 'Stanic', 'broj_kartice': '100000000', 'CVV': '100'}
    ]

    zadaci = [asyncio.create_task(secure_data(p)) for p in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrime: {round(t2-t1, 2)} sek")
