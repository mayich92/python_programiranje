# Zadatak 17
# Napravite program koji simulira igru 10 sekundi, 
# cilj igre je mentalno izbrojiti 10 sekundi i biti što bliži

# import time
# wait = 5
# input("Unesite ENTER za početak.")
# start = time.time()
# input(f'Unesite ENTER kad mislite da je prošlo točno {wait} sekundi.')
# end = time.time()
# duration = end - start
# duration = round(duration, 2)

# difference = round(duration - wait, 2)

# print(f"Proteklo je {duration} sekundi.")

# if difference > 0:    # duration > 10    # duration > wait
#     print(f"Pritisnuli ste tipku {difference} sekundi prekasno.")
# elif difference < 0:    # duration < 10    # duration < wait
#     print(f"Pritisnuli ste tipku {abs(difference)} sekundi prerano.")
# else:    # difference = 0; duration = 10    # duration = wait
#     print("Svaka čast, pogodili ste u zadnju decimalu.")

# # print(f"Promasili ste za {abs(duration - 10)} sekundi") 


# Zadatak 18
adresar = {
    'Ana': 'Zagreb',
    'Bojan': 'Osijek',
    'Damir': 'Osijek',
    'Egon': 'Split',
    'Fran': 'Zagreb'
}

inverzni_adresar_lc = [(v, k) for k, v in adresar.items()]
inverzni_adresar_dc = {v : k for k, v in adresar.items()}
# print(inverzni_adresar_dc)    # ne radi ako imamo duplikatne vrijednosti u ulaznom dictu

inverzni_adresar_koji_zelimo_dobiti = {
    'Zagreb': ['Ana', 'Fran'],
    'Osijek': ['Bojan', 'Damir'],
    'Split': ['Egon']
}

inverzni_adresar = {}
for k, v in adresar.items():
    if v not in inverzni_adresar.keys():
        inverzni_adresar[v] = [k]
    else:    # v already in keys
        inverzni_adresar[v].append(k)

print(inverzni_adresar)
print(type(inverzni_adresar))

# u slučaju korištenja seta umjesto liste
inverzni_adresar_setova = {}
for k, v in adresar.items():
    if v not in inverzni_adresar_setova.keys():
        inverzni_adresar_setova[v] = {k}
        # inverzni_adresar_setova = set()
        # inverzni_adresar_setova[v].add(k)
    else:    # v already in keys
        inverzni_adresar_setova[v].add(k)

print(inverzni_adresar_setova)
print(type(inverzni_adresar_setova))