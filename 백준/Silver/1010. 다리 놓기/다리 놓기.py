def factorial(n, k):
    if n == k:
        return k
    else:
        n = n * factorial(n-1, k)
        return n

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(factorial(B, B-A+1)//factorial(A, 1))
    