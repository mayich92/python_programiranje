uvjet1 = 5 < 3
uvjet2 = 'a' in 'rečenica'

if uvjet1:
    pass
elif uvjet2:
    pass
else:
    pass


# if uvjet1:
#     print('Uvjet 1 je ispunjen')
# elif uvjet2:
#     print('Uvjet 2 je ispunjen')
# else:
#     print('Nijedan uvjet nije ispunjen')

brojevi = []
for broj in range(1, 30+1):
    brojevi.append(broj)

brojevi_lc = [i for i in range(1, 31)]
brojevi_range = list(range(1, 31))

# print(brojevi)
# print(brojevi_lc)
# print(brojevi_range)
# print(brojevi == brojevi_lc == brojevi_range)
# print(5 < 10 < 20)
# print(5 < 10 and 10 < 20)    # nepotrebno pisati, moguće ulančavanje

# for broj in brojevi:
#     if broj % 9 == 0:
#         print(f"Broj {broj} je djeljiv s 9.")
#     elif broj % 6 == 0:
#         print(f"Broj {broj} je djeljiv s 6.")
#     elif broj % 3 == 0:
#         print(f"Broj {broj} je djeljiv s 3.")
#     else:
#         print(f"Broj {broj} nije djeljiv s 3, 6 ili 9.")

# for broj in brojevi:
#     if broj % 9 == 0:
#         print(f"Broj {broj} je djeljiv s 9.")
#     if broj % 6 == 0:
#         print(f"Broj {broj} je djeljiv s 6.")
#     if broj % 3 == 0:
#         print(f"Broj {broj} je djeljiv s 3.")
#     else:
#         print(f"Broj {broj} nije djeljiv s 3, 6 ili 9.")

# for broj in brojevi:
#     if broj % 3 == 0 and broj % 6 == 0 and broj % 9 == 0:
#         print(f"Broj {broj} je djeljiv s 3, 6 i 9.")

# brojevi = list(range(1, 1_000_000+1))
# for broj in brojevi:
#     if broj % 67 == 0 and broj % 78 == 0 and broj % 9 == 0:
#         print(f"Broj {broj} je broj koji tražite")

# text = "Ovo je neka rečenica"
# for word in text.split():
#     if len(word) <= 5:
#         print(word)

# opisi = {
#     'py': 'Python source kod',
#     'docx': 'Microsoft Word dokument',
#     'pdf': 'Portable Document Format'
# }

# filename = input("Unesite ime datoteke: ")
# filename = filename.lower()
# parts = filename.split('.')
# extension = parts[-1]

# if extension == 'py':
#     description = 'Python source kod'
# elif extension == 'docx':
#     description = 'Microsoft Word dokument'
# elif extension == 'pdf':
#     description = 'Portable Document Format'
# else:
#     description = "nepoznat tip datoteke"

# # extension = filename.split('.')[-1]
# # description = opisi.get(extension, "nepoznat tip datoteke")
# print(f"Vaša datoteka ima ekstenziju .{extension} i to je {description}.")

# text = input("Unesite riječ: ")
# text = text.lower()
# to_remove = ' .-_?!*,'
# for c in to_remove:
#     text = text.replace(c, '')
# text_reversed = text[::-1]
# if text == text_reversed:
#     print(f"String {text} JE palindrom.")
# else:
#     print(f"String {text} NIJE palindrom")

for i in range(1, 10**3):
    print(i)
