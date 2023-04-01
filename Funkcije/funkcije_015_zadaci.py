# Problem 3 (Euler)

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# 12 = 2 * 2 * 3

broj = 600851475143


def prosti_faktori(broj):
    i = 2
    pf = []
    while broj != 1:
        while broj % i == 0:
            print(broj, i)
            pf.append(i)
            broj = int(broj / i)
        i += 1

    print("Prosti faktori su: ", pf)
    print("Najveći prosti faktor: ", pf[-1])


# prosti_faktori(broj)

# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(broj):
    return str(broj) == str(broj)[::-1]


def pal_numbers(digits):
    palindromski_brojevi = []
    for i in range(10 ** (digits - 1), 10 ** digits):
        for j in range(10 ** (digits - 1), 10 ** digits):
            umnozak = i * j
            if is_palindromic(umnozak):
                palindromski_brojevi.append(umnozak)
    return palindromski_brojevi


# palindromski_brojevi = pal_numbers(4)
# print("Palindromski brojevi su: ", palindromski_brojevi)
# print("Najveći palindromski broj: ", palindromski_brojevi[-1])

# Problem 8.
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this product?

broj = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''


def potraga(broj, znamenki):
    broj = broj.replace(' ', '').replace('\n', '')
    umnosci = []
    for i in range(len(broj)):
        vrijednost = int(broj[i])
        umnozak = 1
        if i + znamenki > len(broj):
            break
        for j in range(i, i + znamenki):
            umnozak *= int(broj[j])
        umnosci.append(umnozak)
        # print(i, umnozak)
    return umnosci


print(max(potraga(broj, 13)))
