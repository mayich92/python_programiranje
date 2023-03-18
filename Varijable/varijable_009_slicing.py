lista = [123, 45.6, "tekst", "drugi tekst", "123abc", True, False, "54", "true", 78]
prvi_clan = lista[0]
prva_dva_clana = lista[0:2]
print(prva_dva_clana)
prva_dva_clana = lista[:2]
od_drugog_do_kraja = lista[2:]
od_drugog_do_kraja = lista[2:len(lista)]        #zadnji dopušteni index je len(lista)-1
od_treceg_do_petog = lista[3:6]
print(od_drugog_do_kraja)
print(lista[2] , lista[5])

# slicing [a:b] -- lista [a] je ukljuceno, lista [b] nije

zadnja_dva_clana = lista[-2:]
sve_osim_zadnja_dva_clana = lista[:-2]

sve = lista[-len(lista):len(lista)]    #jednostruka cijela lista
svaki_drugi = lista[0:len(lista):2]
print(svaki_drugi)
print(sve)
print(zadnja_dva_clana)
print(sve_osim_zadnja_dva_clana)

obrnuto =lista[::-1]     #zapamtiti
obrnuto_svaki_drugi = lista[::-2]
print(obrnuto)
print(obrnuto_svaki_drugi)



