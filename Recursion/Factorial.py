def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

n = int(input("Enter The Number : "))
print(factorial(n))