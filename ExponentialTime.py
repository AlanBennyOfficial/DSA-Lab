import time

def ExponentialTime(n):
    start = time.time()
    def Exp(n):
        if n <= 1:
            return 1
        else:
            return  Exp(n-1)+Exp(n-1)
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

ExponentialTime(10)
ExponentialTime(100)
ExponentialTime(1000)

# OUTPUT

# Time taken for n = 10: 4.76837158203125e-07 seconds
# Time taken for n = 100: 4.76837158203125e-07 seconds
# Time taken for n = 1000: 7.152557373046875e-07 seconds