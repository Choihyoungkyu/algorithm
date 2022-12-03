# def solution(phone_book):
#     # answer = True
#     # for num1 in phone_book:
#     #     for num2 in phone_book:
#     #         if num2 == num1:
#     #             continue
#     #         if num2[:len(num1)] == num1:
#     #             answer = False
#     #             return answer
#     # return answer
    
#     answer = True
#     dic = {}
#     for num in phone_book:
#         dic[num] = 1
        
#     for num in phone_book:
#         tmp = ''
#         for i in range(len(num)-1):
#             tmp += num[i]
#             if tmp in dic:
#                 answer = False
#                 return answer
#     return answer

2
3
4
5
6
7
8
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True