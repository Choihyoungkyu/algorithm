S1 = list(input())
S2 = list(input())

def LCS(S1, S2):
    arr = [[0] * (len(S2)+1) for _ in range(len(S1)+1)]
    maxV = 0
    for i in range(1, len(S1)+1):
        for j in range(1, len(S2)+1):
            if S2[j-1] != S1[i-1]:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
            else:
                arr[i][j] = arr[i-1][j-1] + 1
            maxV = max(arr[i][j], maxV)
    return maxV

print(LCS(S1, S2))