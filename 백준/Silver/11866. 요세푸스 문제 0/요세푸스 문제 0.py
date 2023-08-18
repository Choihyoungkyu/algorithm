N, K = map(int,input().split())
i = 0
answer = []
visited = [0] * N
tmp = 0
while len(answer) < N:
    if not visited[i]:
        tmp += 1
        if tmp == K:
            visited[i] = 1
            answer.append(i+1)
            tmp = 0
    i = (i+1)%N
ans = "<"
for i in range(N):
    ans += str(answer[i]) + ", " if i<N-1 else str(answer[i])
ans += ">"
print(ans)