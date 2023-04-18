import datetime as dt

# string_datum = "11.04.2023."
# datum = dt.datetime.strptime(string_datum, "%d.%m.%Y.")

# petak = dt.date(2023, 4, 14)
# dan_u_tjednu = dt.date.weekday(petak)

dani = {
    0: 'ponedjeljak',
    1: 'utorak',
    2: 'srijeda',
    3: 'četvrtak',
    4: 'petak',
    5: 'subota',
    6: 'nedjelja',
}

dani = ['pon', 'uto', 'sri', 'čet', 'pet', 'sub', 'ned']

print("Dobrodošli u program za provjeru dana u tjednu!")
while True:
    datum = input("Unesite datum u formatu \"DD.MM.YYYY.\"\t")
    datum = dt.datetime.strptime(datum, "%d.%m.%Y.")
    dan, mjesec, godina = datum.day, datum.month, datum.year
    datum = dt.date(year=godina, month=mjesec, day=dan)
    indeks_dan_u_tjednu = dt.date.weekday(datum)
    ime_dana = dani[indeks_dan_u_tjednu]
    print(f"Uneseni datum je {ime_dana}.")
    izlaz = input("Želite li provjeriti još datuma? (DA/NE)\t")
    if izlaz.upper() == "NE":
        break
print("Hvala na korištenju alata!")