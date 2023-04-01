# Napisati funkciju koja ispituje je li broj prost (prim-broj) ili ne
# primbroj je djeljiv samo sa sobom i s 1

def is_prime(broj):
    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True

def divisors(broj):
    dv = []
    for i in range(2, int(1+broj**0.5)):
        if broj % i == 0:
            dv.append(i)
    return dv

def program():
    print("Dobrodošli u ispitivač prostih brojeva! ")
    while True:
        unos = int(input("Unesite broj (unesite 0 za kraj programa): "))
        if unos == 0:
            print("Hvala na korištenju programa! ")
            break
        elif unos < 0:
            print("Prosti brojevi moraju biti pozitivni cijeli brojevi! ")
            continue
        djelitelji = divisors(unos)
        # prost = is_prime(unos)
        if djelitelji:
            print(f"Broj {unos} NIJE prost broj!")
            print("Djelitelji su: ", end='')
            print(*djelitelji, sep=' ')
        else:
            print(f"Broj {unos} JE prost broj!")
        print('-'*50)

program()