def solve(num1, num2):
    floor_0 = [i for i in range(1, num2+1)]
    # 0층의 사람 채워넣기까지는 생각했다      

    for k in range(num1):
        for j in range(1,num2):
            floor_0[j] += floor_0[j-1]
            #굳이 공간복잡도 늘리지 않고 0층 배열에 더해가는구나

            print(k, j, floor_0[j])
            #여기서 출력되는 값은 k+1 층의 j호에 사는 사람이 데려와야 할 사람 수


    return floor_0[-1]


def main():
    print(solve(5, 3))

if __name__ == "__main__":
    main()
