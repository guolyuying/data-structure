# Fibonacci Sequence: simple but slow solution. T(n) = O(2^n)
def fib(n):
    if n>=3:
        return fib(n-1)+fib(n-2)
    else:
        return 1

print(fib(4))

# Fibonacci Sequence: Memoized Solution. T(n) = O(n)
# If n is too big (>=1000), the call stack will overload and cause error
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result
def fib_memo(n):
    memo = [None] * (n+1)   # initialize an array named "memo" to store repeated calculation results
    return fib_2(n, memo)

print(fib_memo(100))

# Fibonacci Sequence: Bottom-up Solution. T(n) = O(n)
# does not cause call stack to overload because the calculations don't involve calling a function
# instead, the program calculates by adding values that are already stored in an established array
def fib_bottom_up(n):
    if n == 1 or n ==2:
        return 1
    bottom_up = [None] * (n+1)  # initialize an array named "bottom_up" to store values of a fibonacci sequence
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print(fib_bottom_up(1000))