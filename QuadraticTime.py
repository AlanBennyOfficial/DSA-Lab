import time

def QuadraticTime(n):
    start = time.time()
    for i in range(n):
        for j in range(n):
            pass
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

QuadraticTime(1000)
QuadraticTime(10000)
QuadraticTime(100000)

# OUTPUT

# Time taken for n = 1000: 0.008435487747192383 seconds
# Time taken for n = 10000: 0.9317052364349365 seconds
# Time taken for n = 100000: 95.50999069213867 seconds