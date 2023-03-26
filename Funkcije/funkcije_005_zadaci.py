# Zadatak 12.
# pronaći najmanjih N cijelih brojeva koji zadovoljavaju kriterije:
# 1. djeljiv s 41
# 2. sadrži 189 u sebi
# 3. palindromski broj
# ekstra bodovi: da su kriteriji varijabilni s obzirom na korisnički unos

def is_palindromic(number):
    return str(number) == str(number)[::-1]
    # if str(number) == str(number)[::-1]:
    #     return True
    # else:
    #     return False

# for i in range(1, 10**7+1):
#     str_i = str(i)
#     if i % 41 == 0 and '189' in str_i and is_palindromic(i):
#         print(i)

i = 0
N = int(input("Unesite koliko želite elemenata: "))
faktor = int(input("Unesite broj s kojim mora biti djeljiv: "))
podstring = input("Unesite broj koji mora sadržavati: ")
validni = []
while True:
    if podstring in str(i) and is_palindromic(i):
        validni.append(i)
        if len(validni) == N:
            break
    i += faktor

print(*validni, sep='\n')
