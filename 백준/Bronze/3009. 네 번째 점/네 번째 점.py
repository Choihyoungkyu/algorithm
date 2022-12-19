dic1 = {}
dic2 = {}
for _ in range(3):
    a, b = map(int, input().split())
    if a not in dic1:
        dic1[a] = 0
    if b not in dic2:
        dic2[b] = 0
    dic1[a] += 1
    dic2[b] += 1

num1 = 0
num2 = 0
for key in dic1.keys():
    if dic1[key] == 1:
        num1 = key
        break
for key in dic2.keys():
    if dic2[key] == 1:
        num2 = key
        break
print(num1, num2)