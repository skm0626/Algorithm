from itertools import permutations
def sosu(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def solution(numbers):
    answer = []
    num = [i for i in numbers]
    num_per  = []
    for i in range(1,len(numbers)+1):
        num_per+=(list(permutations(num,i)))
    # num_per+=numbers
    num_per = [int(''.join(i)) for i in num_per]
    # print(num_per)
    num_per = list(set(num_per))
    # print(num_per)
    for i in num_per:
        if sosu(i)==True:
            answer.append(i)
    return len(set(answer))
