import itertools

def solution(expression):
    answer = 0
    # 숫자 리스트, 연산 리스트 나누기
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
    
    # 연산 기호별 계산 함수
    def oper(op, num1, num2):
        if op == "*":
            return num1*num2
        elif op == "+":
            return num1+num2
        elif op == "-":
            return num1-num2
    
    # 경우의 수
    for permutation in itertools.permutations(["*", "+", "-"]):
        res_tmp = 0
        nums_tmp = nums[:]
        ops_tmp = ops[:]
        # 우선순위별 계산 후 리스트에 추가하는 방식
        for i in range(3):
            j = -1
            while j < len(ops_tmp)-1:
                j += 1
                # 계산을 한 후 숫자리스트에 추가하고 해당 인덱스에서 다시 시작
                if ops_tmp[j] == permutation[i]:
                    num1 = nums_tmp.pop(j)
                    num2 = nums_tmp.pop(j)
                    op = ops_tmp.pop(j)
                    nums_tmp.insert(j, oper(op, num1, num2))
                    j -= 1
        if answer < abs(nums_tmp[0]):
            answer = abs(nums_tmp[0])
            
    return answer