# Zadatak 7.
# Simulirati dječju igru "Fizz Buzz". Korisnik u konzolu unosi završni broj, pa kreće brojanje od 1.
# Umjesto svakog broja koji je djeljiv s 3 treba reći (ispisati u konzolu) "Fizz" , a umjesto svakog broja djeljivog s 5 treba reći "Buzz".
# U slučaju da je broj djeljiv s oba broja, obje riječi trebaju biti ispisane ("FizzBuzz").
# U slučaju da broj nije djeljiv ni s 3 ni s 5, treba ispisati taj broj.
# Dodatni kontekst/fun facts:
# pošto postoji jako velik broj načina na koje je moguće riješiti ovaj zadatak, popularan je izbor za izazove kodiranja,
# code golf te programerske intervjue
# https://en.wikipedia.org/wiki/Fizz_buzz
# postoji i naša lokalizirana inačica "Štoflec"/"Štoflek", ali je ona češće drinking game nego dječja igra
# Primjer izvođenja:
# Unesite završni broj: 20
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
#

last_num = int(input("Enter last number in the game: "))
for num in range(1,last_num+1):
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz")
    elif num % 3 == 0:
        print(f"Fizz")
    elif num % 5 == 0:
        print(f"Buzz")
    else:
       print(num)

