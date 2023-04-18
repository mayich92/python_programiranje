
from is_prime import is_prime_num

gg = 100
prim_brojevi = []
for i in range(2, gg+1):
    if is_prime_num(i):
        prim_brojevi.append(str(i))

print('-'.join(prim_brojevi))
