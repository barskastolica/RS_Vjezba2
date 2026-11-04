"""
Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika
na poslužiteljskoj strani.
Korutina kao ulazni parametar prima rječnik koji opisuje korisnika,
a sastoji se od ključeva korisnicko_ime, email i lozinka.
Unutar korutine simulirajte provjeru korisničkog imena na način da ćete provjeriti
nalaze li se par korisnicko_ime i email u bazi korisnika.
Ova provjera neka traje ~3 sekunde (simulacija upita prema bazi podataka u Cloudu).

Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."

Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija()
koja će simulirati autorizaciju korisnika u trajanju od 2 sekunde.
Funkcija kao ulazni parametar prima rječnik korisnika iz baze i lozinku
proslijeđenu iz korutine autentifikacija().
Autorizacija simulira dekripciju lozinke (samo provjerite podudaranje stringova)
i provjeru s lozinkom iz baza_lozinka.
Ako su lozinke jednake, korutine vraća poruku
"Korisnik {korisnik}: Autorizacija uspješna.", a u suprotnom
"Korisnik {korisnik}: Autorizacija neuspješna.".

Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.
"""
import asyncio
import time

baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_baza, upisana_lozinka):
    await asyncio.sleep(2)
    korisnicko_ime = korisnik_baza['korisnicko_ime']

    spremljena_lozinka = next(
        (zapis_lozinke['lozinka']
         for zapis_lozinke in baza_lozinka
         if zapis_lozinke['korisnicko_ime']==korisnicko_ime),
         None
    )
    if spremljena_lozinka == upisana_lozinka:
        return f"Korisnik {korisnicko_ime}: Autorizacija uspjesna"
    return f"Korisnik {korisnicko_ime}: Autorizacija neuspjesna"

async def autentifikacija(uneseni_podaci):
    await asyncio.sleep(3)

    korisnik_baza = next(
        (zapis_korisnika
         for zapis_korisnika in baza_korisnika
         if zapis_korisnika['korisnicko_ime']==uneseni_podaci['korisnicko_ime']
         and zapis_korisnika['email']==uneseni_podaci['email']),
         None
    )
    if korisnik_baza is None:
        return f"Korisnik {uneseni_podaci['korisnicko_ime']} nije pronaden"
    return await autorizacija(korisnik_baza, uneseni_podaci['lozinka'])

async def main():
    podaci_za_prijavu = {
        'korisnicko_ime': 'ana_anic',
        'email': 'aanic@gmail.com',
        'lozinka': 'super_teska_lozinka'
    }
    poruka = await autentifikacija(podaci_za_prijavu)
    print(poruka)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrime: {round(t2-t1, 2)} sek")