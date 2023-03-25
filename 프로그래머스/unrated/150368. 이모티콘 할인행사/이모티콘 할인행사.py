from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount_list = [[10, 20, 30, 40] for _ in range(len(emoticons))]
    
    for discounts in product(*discount_list):
        tmp = [0, 0]
        for user in users:
            price = 0
            for i in range(len(emoticons)):
                if user[0] <= discounts[i]:
                    price += (100 - discounts[i]) * 0.01 * emoticons[i]
            
            if price >= user[1]:
                tmp[0] += 1
            else:
                tmp[1] += price
                
        if tmp[0] > answer[0]:
            answer = [tmp[0], int(tmp[1])]
        elif tmp[0] == answer[0] and tmp[1] > answer[1]:
            answer[1] = int(tmp[1])
            
    return answer