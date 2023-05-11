N = int(input())

count = 0
for i in range(1, N+1):
    if i < 100:
        count += 1
    else:
        s = int(str(i)[0]) - int(str(i)[1])
        for j in range(1, len(str(i))-1):
            if int(str(i)[j]) - int(str(i)[j+1]) == s:
                pass
            else:
                break
        else:
            count += 1

print(count)