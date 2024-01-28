N = int(input())

arr = [0]*31 
arr[2] = 3
arr[4] = 11 

if N >= 6:
    for n in range(6, N+1, 2):
        arr[n] = arr[n-2]*4 - arr[n-4]

print(arr[N])
        