import random

answer = []

while len(answer) < 4 :
  x = random.randint(1,9)
  if(x not in answer) :
    answer.append(x)

unsolved = True
strike = [False] *4
tryNum = 1

def checkS(arr) :
  strike[0] = False
  strike[1] = False
  strike[2] = False
  strike[3] = False
  for i in range(len(answer)) :
    if answer[i] == arr[i] :
      strike[i] = True
  return strike.count(True)

def checkB(arr) : 
  balls = 0
  checkedNum = []
  for i in range(len(answer)) :
    if strike[i] is False :
      if (arr[i] in answer) and (arr[i] not in checkedNum) :
        balls += 1
  return balls

while unsolved: 
  if tryNum <= 10 :
    inputNumbers = str(input(str(tryNum) + '번째 시도 : 숫자를 입력하세요 (0은포기) ')).replace(" " , "")
    if('0' in inputNumbers) :
      print('포기합니다.')
      break
    elif len(inputNumbers) < 4:
      print('숫자를 4개 입력해주세요.')
      break
    inArr = list(map(int, inputNumbers[:4])) # 입력 길이 제한
    if checkS(inArr) == 4 :
      print(inputNumbers + " 정답입니다.")
      unsolved = False
    elif (checkB(inArr) == 0) and (checkS(inArr) == 0) :
      print('Out')
      tryNum += 1
    else :
      print(str(checkS(inArr))+'S '+str(checkB(inArr))+'B')
      tryNum += 1
  else :
    print('횟수 초과! 실패')
    break
