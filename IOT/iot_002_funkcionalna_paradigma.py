
# def invert(text):
#     return text[::-1]

invert = lambda text: text[::-1]

# print(invert('Test'))

# MAP, FILTER, REDUCE

values = ['Test', '123test', '1!']

# for i in range(len(values)):
#     values[i] = invert(values[i])

# values = [invert(i) for i in values]

values = list(map(invert, values))

# print(values)

values = [1.2, 3.4, 5.6]
values = list(map(lambda x: x**2, values))
# print(values)

kvadrati = [i**2 for i in range(1, 11)]
# print(kvadrati)
# mali_kvadrati = []
# for k in kvadrati:
#     if k < 50:
#         mali_kvadrati.append(k)

mk = lambda x: x < 50

# def mk(x):
#     return x < 50

# bool_values = list(map(mk, kvadrati))
filtrirani_kvadrati = list(filter(mk, kvadrati))
# print(filtrirani_kvadrati)

values = [
    '123',
    '234.5',
    'abc',
    '1a',
    '78.91'
]

# numerical_values = []
# for v in values:
#     if v.replace('.', '').isdigit():
#         numerical_values.append(float(v))
# print(numerical_values)

values = list(filter(lambda x: x.replace('.', '').isdigit(), values))
# values = [float(i) for i in values]
values = list(map(float, values))
print(values)