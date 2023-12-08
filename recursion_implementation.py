# Factorial
def fact(n):
    if n>=1:
        return n*fact(n-1)
    else:
        return 1

print(fact(4))

# Fibonacci Sequence
# For more efficient solutions, see Dynamic_Programming.py
def fib(n):
    if n>=3:
        return fib(n-1)+fib(n-2)
    else:
        return 1

print(fib(4))