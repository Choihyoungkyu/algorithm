N = input()
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = []
count = 1
for i in N:
    s.append(i)
for i in range(len(s)-1):
    if s[i] + s[i+1] in l:
        pass
    elif i <= len(s)-3:
        if s[i] + s[i+1] + s[i+2] == 'dz=':
            pass
        else:
            count += 1
    else:
        count += 1
print(count)