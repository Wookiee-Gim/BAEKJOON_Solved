n = int(input()) # 입력 받는 숫자의 개수
m = input() # 공백없이 주어진 N개의 숫자

# 공백없이 주어진 N개의 숫자를 문자열로 입력받아 슬라이싱을 통해 각 자리수 합 구함

Sum = 0 # 각자리 수 합을 구하기 위한 초기 값

for i in range(n): # 각 자리 수 합이기 때문에 범위 n 까지
    Sum += int(m[i]) # 각 자리 합을 형변환을 통해 더해줌

print(Sum)
