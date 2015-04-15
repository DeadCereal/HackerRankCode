numcases = int(input())

for _ in range(numcases):
    N,K=map(int, input().split())
    timelist = list(map(int, input().split()))
    ontimecount=0
    for x in timelist:
        if x <= 0:
            ontimecount += 1
    
    if ontimecount >= K:
        print("NO")
    else:
        print("YES")
    
    
