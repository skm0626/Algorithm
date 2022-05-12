def quadratic(a,b,c):
    D = ((b**2)-4*a*c)**0.5
    X1 = (-b + D) / 2*a
    X2 = (-b - D) / 2*a
    dap = max(X1,X2)
    return dap
    
def solution(brown, yellow):
    answer = []
    x = quadratic(1,-2-brown//2,brown+yellow)
    y = (brown+yellow)//x
    answer.append(x)
    answer.append(y)
    return answer
