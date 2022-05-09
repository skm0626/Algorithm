# https://hyunsix.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0%EC%88%98%EB%A7%8C%EB%93%A4%EA%B8%B0-python
def solution(number, k):
    answer = []
    for i in number:
        while answer and k>0 and answer[-1]>i:
            answer.pop()
            k-=1
        answer.append(i)
    answer = ''.join(answer[:len(answer)-k])
    return answer
