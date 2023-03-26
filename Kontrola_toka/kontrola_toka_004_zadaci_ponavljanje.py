# Zadatak 7. - FizzBuzz (Fizz na djeljive s 3, Buzz na djeljive s 5, inače broj koji je na redu)

# limit = int(input("Unesite gornju granicu: "))
# for i in range(1, limit+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# Zadatak 8. - najveća vrijednost u listi (max, sort, manualno)
# unos = '3,1,2.5, 8'
# vrijednosti = unos.split(',')
# # vrijednosti = [v.strip() for v in vrijednosti]
# brojcane_vrijednosti = [float(v) for v in vrijednosti]
# print(brojcane_vrijednosti)
# print(max(brojcane_vrijednosti))
# print(sorted(brojcane_vrijednosti)[-1])

# najveci = brojcane_vrijednosti[0]
# for broj in brojcane_vrijednosti:
#     if broj > najveci:
#         najveci = broj
# print(najveci)

# Zadatak 9. - izračun zbroja znamenki broja u konzoli

# unos = '456 ?!+0e78'
# # unos = unos.replace('.', '')
# zbroj = 0
# for c in unos:
#     if c.isdigit():
#         zbroj += int(c)
# print(zbroj)

# unos = '123'
# vrijednosti = [int(c) for c in unos]
# print(sum(vrijednosti))

# Zadatak 10. - svaka druga riječ u rečenici obrnuta
# text = 'the quick brown fox jumps over the lazy dog'    # pangram
# words = text.split()

# for i in range(len(words)):
#     if i % 2 == 1:
#         words[i] = words[i][::-1]

# new_text = ' '.join(words)
# print(new_text)

# new_words = []
# for i, word in enumerate(words):
#     if i % 2 == 1:
#         new_words.append(word[::-1])
#     else:
#         new_words.append(word)
# new_text = ' '.join(new_words)
# print(new_text)


# DODATNO - ternarni izrazi
# unos = '456abc123'
# lc = [int(c) if c.isdigit() else 0 for c in unos]
# print(sum(lc))

text = 'the quick brown fox jumps over the lazy dog'
lst = [word[::-1] if i % 2 == 1 else word for i, word in enumerate(text.split())]
print(' '.join(lst))
