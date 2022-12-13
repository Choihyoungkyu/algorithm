import itertools

def solution(expression):
    answer = 0
    nums = []
    ops = []
    tmp = ""
    for i in expression:
        if not 48 <= ord(i) <=57:
            ops.append(i)
            nums.append(int(tmp))
            tmp = ""
        else:
            tmp += i
    if tmp:
        nums.append(int(tmp))
    
    def oper(op, num1, num2):
        if op == "*":
            return num1*num2
        elif op == "+":
            return num1+num2
        elif op == "-":
            return num1-num2

    for permutation in itertools.permutations(["*", "+", "-"]):
        res_tmp = 0
        nums_tmp = nums[:]
        ops_tmp = ops[:]
        for i in range(3):
            j = -1
            while j < len(ops_tmp)-1:
                j += 1
                if ops_tmp[j] == permutation[i]:
                    num1 = nums_tmp.pop(j)
                    num2 = nums_tmp.pop(j)
                    op = ops_tmp.pop(j)
                    nums_tmp.insert(j, oper(op, num1, num2))
                    j -= 1
        if answer < abs(nums_tmp[0]):
            answer = abs(nums_tmp[0])
            

    return answer