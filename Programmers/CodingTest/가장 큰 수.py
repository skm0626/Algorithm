from itertools import permutations

def solution(numbers):
    # answer = ''
    # arr = list(permutations(numbers,len(numbers)))
    # list_arr = [''.join(map(str,i)) for i in arr]
    # answer = max(list_arr)
    # https://esoongan.tistory.com/103
    num = list(map(str,numbers))
    num.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(num))) 
    # int->str하는 이유 : 000의 경우 0으로 해주기 위해서
    return answer
