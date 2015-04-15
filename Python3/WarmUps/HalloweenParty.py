numcases = int(input())

for _ in range(numcases):
    numcuts = int(input())
    
    if numcuts%2 > 0:
        x=int(numcuts/2)
        y=int((numcuts/2)+1)
        print(x*y)
    else:
        x=int(numcuts/2)
        print(x*x)
