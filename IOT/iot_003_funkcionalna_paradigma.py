from functools import reduce

def zbroj(a, b):
    return a + b

umnozak = lambda a, b: a*b

values = [1, 2, 3, 7]
s = reduce(zbroj, values)
u = reduce(umnozak, values)
u2 = reduce(lambda x, y: x*y, values)

values = [1, 3, 5, 6, 2]
greater = lambda a, b: a if a > b else b
greatest_value = reduce(greater, values)
print(greatest_value)