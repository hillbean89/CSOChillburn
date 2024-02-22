import sys
def solution(a, b, a_minus_b):
    if (a-b > 0):
        answer = "VEIT EKKI"
    elif(a-b== a_minus_b):
        answer= "jedi"
    else:
        answer= "sith"
    return answer
    
def test():
    assert solution (38,68,30)== "sith"
    assert solution (69,80,-11)== "jedi"
    assert solution (67,17,50)== "Veit"
    print("all test passed", file= sys.stderr)

def main():
    input()
    a= int(input())
    b= int(input())
    a_minus_b= int(input())
    answer = solution(a,b, a_minus_b)

    print(answer)
#test()

main()
