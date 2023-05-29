# faktorijel -> f(x) = x! = x * x-1 * x-2 * ... * 1 (za prirodne brojeve)
# f(5) = 5 * f(4)
# f(4) = 4 * f(3)
# ...
# f(2) = 2 * f(1)
# f(1) = 1
from functools import reduce

def faktorijel(n):
    values = list(range(1, n+1))
    product = reduce(lambda x, y: x*y, values)
    return product    

# def faktorijel_rekurzivno(n):
#     if n == 1:
#         return 1
#     return n * faktorijel_rekurzivno(n-1)

def faktorijel_rekurzivno(n):
    return n * faktorijel_rekurzivno(n-1) if n > 1 else 1

print(faktorijel_rekurzivno(5))