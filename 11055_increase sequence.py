# 수열 A가 주어졌을 때, 부분수열 중 가장 합이 큰 것을 출력하시오.

# 수열의 크기는 최대 1000이므로 부분집합 갯수는 2^1000

N = int(input())
sequence = list(map(int,input().split()))

total = [0]*N
total[0] = sequence[0] # 아래의 코드에서 N이 1이면 n은 0, n이 0이면 내부의 for문은 작동을 하지 않아 total값 갱신이 안된다. 수동으로 업데이트 해줘야한다.
for n in range(N): # 0 ~ N-1번째 index까지 수열을 탐색한다.
    for m in range(n): # n번째 수열 탐색 시 이전 수열을 탐색하여 증가하는 수열인지 확인한다.
        if sequence[n] > sequence[m]: # 증가하는 수열일 케이스에서는 이 케이스 중 가장 합이 큰 부분수열을 택해야한다.
            total[n] = max(total[n], total[m]+sequence[n])  # 최대 n개의 후보를 탐색하여 현재의 최댓값과 새로 계산한 합을 비교하여 큰 값을 최대값으로 갱신한다.
        else: # 증가하는 수열이 아니면 현재까지의 최대값과 현재 검사하는 단일원소의 크기를 비교하여 최대값을 갱신한다.
            total[n] = max(total[n], sequence[n])

print(max(total))