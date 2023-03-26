# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# brojevi = []
# granica = 1000

# for i in range(1, granica):
#     if i % 3 == 0 or i % 5 == 0:
#         brojevi.append(i)

# print(brojevi, sum(brojevi))


# Problem 9
# tražimo pitagorinu trojku a,b,c, a<b<c (a^2 + b^2 = c^2) za koju vrijedi a+b+c=1000, rješenje: a*b*c

def pitagora(a, b, c):
    return a**2 + b**2 == c**2

def uvjet(a, b, c):
    return a + b + c == 1000

def pretraga1():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - (a+b)
            if pitagora(a,b,c):
                umnozak = a * b * c
                return a,b,c,umnozak

def pretraga2():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = (a**2 + b**2) ** 0.5
            if uvjet(a,b,c):
                umnozak = a * b * c
                return a,b,c,umnozak

def pretraga3():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if uvjet(a,b,c) and pitagora(a,b,c):
                    umnozak = a * b * c
                    return a,b,c,umnozak

import time

start_time = time.time()
print(pretraga2())
end_time = time.time()
duration = end_time - start_time
duration = round(duration, 2)

print(f"Pretraga je trajala {duration} sekundi! ")