# 정수 n에 대하여
# n이 홀수이면 3n+1을 하고
# n이 짝수이면 n을 2로 나눈다.
# n이 1이 될때까지 위의 과정을 반복한다.

def recurPractice(n) :
    print(n)
    #진행 상태를 보고싶으니까
    
    if n == 1:
        return 1
        #기저조건 설정
        
    if n%2 == 1:
        n = int(3*n+1)
    elif n%2 == 0:
        n = int(n/2)

    return recurPractice(n)

def main():
    print(recurPractice(3))

if __name__ == "__main__":
    main()

