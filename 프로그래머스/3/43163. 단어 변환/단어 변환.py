from collections import deque

def solution(begin, target, words):
    answer = 0
    words.append(begin)
    answer = bfs(begin, target, words)
    
    return answer

def bfs(begin, target, words):
    idx = words.index(begin)
    visited = [0] * len(words)
    visited[idx] = 1
    que = deque()
    que.append(begin)
    while que:
        cur_word = que.popleft()
        idx = words.index(cur_word)
        for i in range(len(words)):
            if visited[i]:
                continue
            if check_spell(cur_word, words[i]):
                if words[i] == target:
                    return visited[idx]
                que.append(words[i])
                visited[i] = visited[idx] + 1
    return 0
                
            
def check_spell(cur_word, word):
    flag = False
    for i in range(len(cur_word)):
        if cur_word[i] != word[i]:
            if flag:
                return False
            flag = True
    return True
    