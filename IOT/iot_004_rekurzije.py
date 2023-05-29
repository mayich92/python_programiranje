def print_broja(num):
    print(num)
    if num == 100:
        return
    print_broja(num+1)

print_broja(1)

# glavni program
#    f(1)
#        f(2)
#            f(3)
# ...
#                        f(100)

for i in range(1, 100+1):
    print(i)