# Q. 0 이동시키기
# 여러 개의 0과 양의 정수들이 섞여 있는 배열이 주어졌다고 합시다.
# 이 배열에서 0들은 전부 뒤로 빼내고, 나머지 숫자들의 순서는 그대로 유지한 배열을 반환하는
# 함수를 만들어 봅시다.
# 이 문제는 공간 복잡도를 고려하면서 풀어 보도록 합시다.
# 공간 복잡도 O(1)으로 이 문제를 풀 수 있을까요?

def moveZerosToEnd(nums):
    answer = [];
    meetP = False
    #zero = 0
    total = len(nums)-1
    
    while not meetP :
        if nums[total] != 0:
            meetP=True
        total-=1
    

    for i in range(total, -1, -1) :
        if nums[i] == 0 :
            nums.remove(0)
            nums.append(0)
    #nums += [0] * zero
    return nums
  
  #이렇게 하면 TC 1~4는 통과하지만 TC5는 시간 초과로 터진다.

def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
