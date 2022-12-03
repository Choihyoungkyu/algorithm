def solution(files):
    answer = []
    tmp = []
    idx = 0
    for file in files:
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if 48<=ord(file[i])<=57:
                number += file[i]
                continue
            if number:
                break
            head += file[i]
        tmp.append((head.lower(), int(number), idx))
        idx += 1
        
    for i in sorted(tmp):
        answer.append(files[i[2]])
    
    return answer