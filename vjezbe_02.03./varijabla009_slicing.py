lista = [123, 45.6, "tekst", "drugi tekst", "123abc", True, False, "54", "true", 78]
prvi_clan = lista[0]
prva_dva_clana = lista[0:2]
prva_dva_clana = lista[:2]
od_drugog_do_kraja = lista[2:]
od_drugog_do_kraja = lista[2:len(lista)]
od_treceg_do_petog = lista[3:6]

zadnja_dva_clana = lista[-2:]
sve_osim_zadnja_dva_clana = lista[:-2]

svaki_drugi = lista[:len(lista):2]
svaki_drugi = lista[::2]
svaki_treci = lista[::3]

obrnuto = lista[::-1]   #zapamtiti!
obrnuto_svaki_drugi = lista[::-2]

# slicing [a:b] -> lista[a] je ukljucena, lista[b] je iskljucena

print(obrnuto_svaki_drugi)