import sys
#f = sys.stdin
f = open("C:/algorithm/algo/elice_Algo2/input.txt", 'r')


def favorfood():
    days = f.readline()
    d = [[0]*3]*days

    for i in range(1, days+1):
        for j in range(3):
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue
                    d[]


# 4. 연속 부분 최대합   - 문제: 상훈이는 점심엔 늘 짜장, 짬뽕, 볶음밥 셋 중 하나를 먹는다.
# 하지만 거기엔 규칙이 하나 있는데, 전날 먹은 음식은 먹지 않는다는 것이다.
# 예를 들어 어제 짜장면을 먹었으면, 오늘은 짬뽕이나 볶음밥 중 하나를 먹어야 하는 것이다.
# 짜장, 짬뽕, 볶음밥 선호도는 그날그날 다른데, 매일 선호도가 주어질 때,
# 적절히 날마나 음식을 결정하여 총선호도의 최대값을 구하시오.

def eating(data):
    days = len(data)
    d = [[0] * 3 for i in range(days + 1)]

    for i in range(1, days + 1):
        for j in range(3):
            for k in range(3):
                if j == k:    continue
                d[i][j] = max(d[i][j], d[i-1][k])
            d[i][j] += data[i-1][j]

    return max(d[days][i] for i in range(3))


