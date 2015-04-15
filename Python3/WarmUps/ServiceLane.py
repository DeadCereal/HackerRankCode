N,T=map(int,input().split())
widths=list(map(int,list(input().split())))
for _ in range(0,T):
    i,j=map(int,input().split())
    vehicle=3
    for x in range(i,j+1):
        width=widths[x]
        if width==1:
            vehicle=1
            break
        elif width==2:
            vehicle=2
    print(vehicle)
                
