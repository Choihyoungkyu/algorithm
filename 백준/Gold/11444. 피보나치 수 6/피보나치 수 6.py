# 제곱을 구하는 분할정복
def square(matrix, N):
    if N == 1:
        return matrix
    elif N % 2:
        return multi(square(matrix, N-1), matrix)
    else:
        return square(multi(matrix, matrix), N//2)
    
# 행렬의 곱셈
def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % p
    return temp

# 초기 행렬
matrix = [[1, 1], [1, 0]]

# 피보나치 초기값
start = [[1], [1]]
N = int(input())
p = 1000000007
if N < 3:
    print(1)
else:
    ans = multi(square(matrix, N-2), start)[0][0]
    print(ans)