# fibonaccijev niz (fibonacci sequence)
# 1, 1, 2, 3, 5, 8, 13, 21...
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(1000)
print(result)