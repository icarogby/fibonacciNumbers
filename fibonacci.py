numbers = [0, 1]

def iterativeFibonacci(n):
    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    return numbers[n]

def recursiveFibonacci(n):
    if n < len(numbers):
        return numbers[n]
    
    numbers.append(recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2))

    return numbers[n]

def optimizedFibonacci(n):
    n1 = 0
    n2 = 1

    if n <= 1:
        return n

    for i in range(2, n + 1):
        n1, n2 = n2, n1 + n2
    
    return n2
    
def infinityFibonacci():
    n1 = 0
    n2 = 1

    while(True):
        yield n1
        n1, n2 = n2, n1 + n2
