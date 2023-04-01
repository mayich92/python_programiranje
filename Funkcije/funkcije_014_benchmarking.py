import time

test = 51651684

def divisors1(broj):
    dv = []
    gg = int(1+broj**0.5)
    for i in range(2, gg):
        if broj % i == 0:
            dv.append(i)
    return dv

def divisors2(broj):
    dv = []
    gg = broj
    for i in range(2, gg):
        if broj % i == 0:
            dv.append(i)
    return dv

st1 = time.time()
print(divisors1(test))
et1 = time.time()
d1 = et1-st1
d1 = round(d1, 2)
print(f"Izvođenje je trajalo {d1} sekundi")

st2 = time.time()
print(divisors2(test))
et2 = time.time()
d2 = et2-st2
d2 = round(d2, 2)
print(f"Izvođenje je trajalo {d2} sekundi")

