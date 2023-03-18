vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

zaglavlje_gornja_linija = 'ID\tTip\t\tProizvođač\t\tRegistarska\t\tGodina prve\t\tCijena'
zaglavlje_donja_linija = '  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)'
zaglavlje_donja_crta = '_'*105
print(zaglavlje_gornja_linija, '\n', zaglavlje_donja_linija, '\n', zaglavlje_donja_crta)

# dobivanje preko tupleova (napredniji način)
'''
for key, value in vozni_park.items():
    print(key, value)
'''

for key in vozni_park.keys():
    elements = vozni_park[key]    # value = dict[key]
    print(key, end='\t')
    for e in elements:
        print(e, end='\t\t')
    print()
    # print(key, value)
