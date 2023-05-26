from functools import lru_cache
@lru_cache
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

n=factorial(int(input()))
print(n)