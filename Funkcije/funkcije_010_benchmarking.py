
# import timeit
import time

start_time = time.time()

for i in range(1, int(10**5/4)):
    print(i)

end_time = time.time()
duration = end_time - start_time
print(duration)    # proteklo sekundi