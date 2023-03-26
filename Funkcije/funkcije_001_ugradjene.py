
lst = [1,2,3]
print(*lst, sep='\t')

# input()
# int(), float(), str() ...
# list(), set(), dict(), tuple()

lst1 = list()
lst2 = []
print(lst1, lst2, lst1 == lst2)

set1 = set()
set2 = {}    # type -> dict -> pripaziti na koliziju s dict()
print(set1, set2, set1 == set2, type(set2))

dict1 = dict()
dict2 = {}
print(dict1, dict2, dict1 == dict2)

tuple1 = tuple()
tuple2 = ()
print(tuple1, tuple2, tuple1 == tuple2)

nesto = (1, )
print(nesto, type(nesto))

# enumerate(), range() ... -> ovo sve su funkcije

# .isupper(), .islower() -> metode, vidjet ćemo kasnije zašto (OOP, klase)

# help(enumerate)
print(print())
a = print()
print(a)