# height = int(input("Unesite visinu piramide: "))
# for i in range(height):
#     string = ''
#     string += ' '*(height-(i+1))
#     string += '#'*(i+1)
#     string += ' '*3
#     string += '#'*(i+1)
#     print(string)
#

height = int(input("Visina: "))
for broj in range(1, height+1):
    print(' '*(height-broj) + '#'*broj, end=' '*3)
    print('#'*broj)