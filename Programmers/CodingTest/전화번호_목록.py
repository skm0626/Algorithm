def solution(phone_book):
    answer = True
    # 만약, 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치함
    phone_book.sort()
    for p1, p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            break
    return answer
  
  
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
