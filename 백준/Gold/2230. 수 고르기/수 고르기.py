n, m = list(map(int, input().split()))
nums = [int(input()) for _ in range(n)]
nums.sort()

i, j = 0, 1
minV = nums[-1] - nums[0]

while i < j and j < n:
    k = nums[j] - nums[i]
    if k == m:
        minV = k
        break

    if k > m and minV > k:
        minV = k
    
    elif k < m and j < n-1:
        j += 1
        continue

    if i < j-1:
        i += 1
    elif j < n-1:
        j += 1
    else:
        i += 1

print(minV)