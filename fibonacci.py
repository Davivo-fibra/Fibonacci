def fibonacci(n):
    if n <0:
        return
    elif n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))