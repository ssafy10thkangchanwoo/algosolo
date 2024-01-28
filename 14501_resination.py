def dfs(i, total):
    global ans
    if i == N:
        ans = max(total, ans)
        return 
    
    if i + T[i] <= N: # i번에서 i+1번으로 가는 비용이 T[i]
        dfs(i+T[i], total + P[i])

    dfs(i+1, total) # 안했음

N = int(input())

T = [] 
P = []

for _ in range(N):
    t, p = map(int,input().split())
    # T, P 는 idx에서 idx+1까지 가는데에 대한 시간 및 그에 따른 보상 의미
    
    T.append(t)
    P.append(p)
ans = 0
total = 0
print(T)
print(P)
dfs(0, total)
print(ans)