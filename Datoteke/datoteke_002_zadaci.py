# Zadatak 20.
# solver za kvadratnu jednadžbu
# 0, 1 ili 2 rješenja, ovisno o diskriminanti

# a * x^2 + b * x + c = 0
# D = vrijednost pod korijenom = b^2 - 4ac
# x1,2 = (-b +- sqrt(b^2 - 4ac))/2a
# D = 0 -> eliminira se plus-minus, ostaje jednostruko rješenje -> -b/2a
# D > 0 -> dva realna rješenja
# D < 0 -> kompleksna rješenja, nema realnih rješenja

from math import sqrt

def solver(a, b, c):
    D = b**2 - 4*a*c
    print('Diskriminanta: ', D)
    if D < 0:
        # return []    # realna rješenja

        # kompleksna rješenja - neće raditi s math.sqrt
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        return [x1, x2]
    elif D == 0:
        x = (-b)/(2*a)
        return [x]
    elif D > 0:    # else
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        return [x1, x2]

# 1,3,2 ; 2,4,5 ; 1,2,1

result = solver(2, 4, 5)
print(result)