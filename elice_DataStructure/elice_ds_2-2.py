
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
