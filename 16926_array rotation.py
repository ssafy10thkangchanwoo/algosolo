from collections import deque
N, M, R = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
deq = deque()
loops = min(N, M) // 2 

for i in range(loops):
    deq.clear()
    
    deq.extend(arr[i][i:M-i])
    deq.extend([row[M-i-1] for row in arr[i+1:N-i-1]])
    deq.extend(arr[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in arr[i+1:N-i-1][::-1]])
    
   
    for _ in range(R):
        t = deq.popleft()
        deq.append(t)
     

    for j in range(i,M-i):
        arr[i][j] = deq.popleft() 
    for j in range(i+1, N-i-1):
        arr[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1):
        arr[N-i-1][j] = deq.popleft()
    for j in range(N-i-2, i, -1):
        arr[j][i] = deq.popleft()


for a in arr:
    print(*a)
        
        # print(arr)
        # print(arr[i+1:N-i-1][::-1])
        # print(arr[i+1:N-i-1])
        # print(arr[N-i-2:i:-1])

        # print(arr[i+1])
        # print(arr[i+1][i])
        # print([row[i] for row in arr[i+1:N-i-1:-1]])
        # print([arr[i+1:N-i-1]])
        # print(deq)
