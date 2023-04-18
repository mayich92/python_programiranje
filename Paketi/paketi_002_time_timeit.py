
# import time as t
# print(t.time())

import time

# vrijeme = time.time()
# cvrijeme = time.ctime()
# print(vrijeme)
# time.sleep(2)
# print(cvrijeme)


import timeit

NUMBER = 1_000
t1 = timeit.timeit('"-".join(str(n) for n in range(10**4))', number=NUMBER)
t2 = timeit.timeit('"-".join([str(n) for n in range(10**4)])', number=NUMBER)
t3 = timeit.timeit('"-".join(map(str, range(10**4)))', number=NUMBER)
print(t1)
print(t2)
print(t3)