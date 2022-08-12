k = input()
s = k.lower()
for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        pass
    else:
        print('false')
        break
else:
    print('true')