S = input()*2
len_a = S.count('a') // 2

min_v = len_a
for i in range(len(S)-len_a+1):
    min_v = min(S[i:i+len_a].count('b'), min_v)
print(min_v)
