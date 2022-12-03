import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
nums1 = list(map(int, input().split()))
M = int(input())
nums2 = list(map(int, input().split()))
result = [0] * M

dic = {}
for num in nums1:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1

for i in range(M):
    if nums2[i] in dic:
        result[i] = dic[nums2[i]]
print(*result)