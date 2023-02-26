def get_length(num):
    n = 0
    while True:
        n += 1
        if 2**(2**n-1) > num:
            return 2**n-1
        
def sub_tree(tree, tot):
    root = int(tree[len(tree)//2])
    if len(tree) > 1 and root == 0 and tree.count('1'):
        tot += 1
    elif len(tree) > 1:
        tot += sub_tree(tree[0:len(tree)//2], tot)
        tot += sub_tree(tree[len(tree)//2+1:], tot)
    return tot

def solution(numbers):
    answer = []
    
    for num in numbers:
        length = get_length(num)
        binary_num = bin(num).lstrip('0').lstrip('b')
        binary_num = '0'*(length-len(binary_num)) + binary_num
        
        check = sub_tree(binary_num, 0)
        # print(binary_num, check)
        answer.append(0 if check else 1)
    return answer

'''
1 3 7 15 31 ...
2 8 128

1  -  1

2  -  010
3  -  011
4  -  100 X
5  -  101 X
6  -  110
7  -  111

8  -  0001000
9  -  0001001 X
10 -  0001010
11 -  0001011
12 -  0001100 X
13 -  0001101 X
14 -  0001110
15 -  0001111
16 -  0010000 X
17 -  0010001 X
18 -  0010010 X
19 -  0010011 X
20 -  0010100 X
'''