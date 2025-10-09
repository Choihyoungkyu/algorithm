
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for idx in range(len(prices)):
        while stack and prices[stack[-1]] > prices[idx]:
            c_idx = stack.pop()
            answer[c_idx] = idx - c_idx
        stack.append(idx)
    for idx in stack:
        answer[idx] = len(prices) - 1 - idx
    return answer