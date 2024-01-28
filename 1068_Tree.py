N = int(input())

arr = list(map(int,input().split()))
child = [[] for _ in range(N)]
for i in range(N):
    if arr[i] != -1:
        child[arr[i]].append(i)

print(child)