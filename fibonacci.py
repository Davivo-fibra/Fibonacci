def fibonacci(n):
    if n <0:
        return
    elif n in {0, 1}:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
print(fibonacci(10))