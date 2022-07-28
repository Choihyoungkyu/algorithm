N = int(input())
x_list = []
y_list = []
for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

rank_list = []
for i in range(N):
    count = 1
    for j in range(N):
        if x_list[i] < x_list[j] and y_list[i] < y_list[j]:
            count += 1
    rank_list.append(count)
for i in rank_list:
    print(i, end=' ')