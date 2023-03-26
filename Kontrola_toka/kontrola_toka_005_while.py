
# brojac = 0
# granica = 7

# while brojac < granica:
#     print(brojac, 'hello')
#     brojac += 1

# print('-'*50)

# for i in range(granica):
#     print(i, 'hello')


# for i in range(10):
#     if i % 3 == 0:
#         continue
#     kvadrat = i ** 2
#     print(i, kvadrat)

# print('-'*50)

# for i in range(10):
#     if i % 3 != 0:
#         kvadrat = i**2
#         print(i, kvadrat)

# print('-'*50)

# brojac = -1
# while brojac < 10:
#     brojac += 1
#     if brojac % 3 == 0:
#         continue
#     kvadrat = brojac ** 2
#     print(brojac, kvadrat)


# brojevi = list(range(1, 10**6 + 1))
# for broj in brojevi:
#     if broj % 13 == 0 and broj % 10 == 4:
#         print(broj)
#         break
#     # print('iteriram dalje', broj)


# brojac = 0
# while True:
#     if brojac % 13 == 0 and brojac % 10 == 4:
#         print(brojac)
#         break
#     brojac += 1


# brojac = 0
# while True:
#     if brojac % 1347 == 0 and str(brojac)[-4:] == '7824':
#         print(brojac)
#         break
#     brojac += 1

import time
# print('a')
# time.sleep(2)
# print('b')

# while True:
#     print('hello')
#     time.sleep(1)

# while True:
#     unos = input('Unesite riječ i ja ću ju obrnuti (unesite KRAJ za kraj petlje): ')
#     if unos == 'KRAJ':
#         break
#     print(f"Vaš obrnuti string je: {unos[::-1]}")

for i in range(5):
    for j in range(3):
        print(i, j)
        # break
    # break