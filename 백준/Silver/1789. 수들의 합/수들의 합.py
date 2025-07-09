N = int(input())

cur = 0 # 현재까지 더해진 자연수들의 합
cnt = 0 # 수의 개수
num = 1   

while cur + num <= N:
    cur += num 
    cnt += 1       
    num += 1        

print(cnt)