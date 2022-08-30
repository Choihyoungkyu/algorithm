import sys
input = lambda: sys.stdin.readline().strip()

# R : 수의 순서를 뒤집는 함수, D : 첫번째 수를 버리는 함수
T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    tmp = input().lstrip('[').rstrip(']')
    if tmp == '':
        arr = []
    else:
        arr = list(map(int, tmp.split(',')))
    K = 0
    cnt = 0
    try:
        for i in p:
            if i == 'R':
                cnt += 1
                if K == 0:
                    K = -1
                else:
                    K = 0
            elif i == 'D':
                arr.pop(K)
        else:
            s = ''
            if cnt % 2 == 0:
                for j in range(len(arr)):
                    if j == len(arr)-1:
                        s += str(arr[j])
                    else:
                        s += str(arr[j]) + ','
            else:
                arr = arr[::-1]
                for j in range(len(arr)):
                    if j == len(arr)-1:
                        s += str(arr[j])
                    else:
                        s += str(arr[j]) + ','
            s = '[' + s + ']'
            print(s)

    except:
        print('error')
