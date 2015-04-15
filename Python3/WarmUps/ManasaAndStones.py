numcases = int(input())
for _ in range(numcases):
    numstones = int(input())-1
    one = int(input())
    two = int(input())
    b = max(one,two)
    a = min(one,two)
    difference = b-a
    maxval = b*numstones
    current = a*numstones
    if(a==b):
        print(str(current))
    else:
        while(current <= maxval):
            print(str(current) + " ", end="")
            current += difference
        print("")
    
