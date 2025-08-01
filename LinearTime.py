import time

# O(n)
def LinearTime(n):
    start = time.time()
    for _ in range(n):
        pass
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

LinearTime(1000)
LinearTime(10000)
LinearTime(100000)

# OUTPUT

# Time taken for n = 1000: 9.775161743164062e-06 seconds
# Time taken for n = 10000: 8.440017700195312e-05 seconds
# Time taken for n = 100000: 0.000850677490234375 seconds