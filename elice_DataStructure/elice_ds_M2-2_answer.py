# 세번째로 큰 숫자 찾아내기
# 0보다 큰 정수들의 배열이 주어졌다고 합시다. 이 배열에서 세번째로 큰 수를 찾아 내 봅시다.
# 
# 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우 가장 큰 수는 50, 두번째로 큰 수는 37, 세번째로 큰 수는 34입니다. 따라서 34를 반환해야 합니다.
# 
# 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.



def thirdMax(nums): #가장 큰 3개의 수를 저장
    maxs = [float('-inf'), float('-inf'), float('-inf')]
    for num in nums:
        if num not in maxs:
            if num > maxs[2]:
                maxs = [maxs[1], maxs[2], num]
            elif num > maxs[1]:
                maxs = [maxs[1], num, maxs[2]]
            elif num > maxs[0]:

                maxs = [num, maxs[1], maxs[2]]
                
    return maxs[0]
def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
