# 세번째로 큰 숫자 찾아내기
# 0보다 큰 정수들의 배열이 주어졌다고 합시다. 이 배열에서 세번째로 큰 수를 찾아 내 봅시다.
# 
# 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우 가장 큰 수는 50, 두번째로 큰 수는 37, 세번째로 큰 수는 34입니다. 따라서 34를 반환해야 합니다.
# 
# 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.


def quick_sort(array, start, end) :
    if start>=end :
        return
    pivot = start
    left = start+1
    right = end

    while (left<=right):
        while(left <= end and array[left] <= array[pivot]):
            left +=1
        while (right > start and array[right]>= array[pivot]):
            right -= 1
        if(left > right) :
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


def thirdMax(nums):
    quick_sort(nums, 0, len(nums)-1)
    return nums[len(nums)-3]

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
