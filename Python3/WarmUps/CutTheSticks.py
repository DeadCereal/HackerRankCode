numints=input()
inlist = input().strip().split()
intlist = [int(n) for n in inlist]
intlist.sort()
for x in range(len(intlist)):
    if intlist[x] != 0:
        lowlength = intlist[x]
        break
        
cutcount=1
while cutcount != 0:
    cutcount=0
    
    for i in range(len(intlist)):
        if intlist[i] > 0:
            intlist[i] = intlist[i] - lowlength
            cutcount += 1
            
    intlist.sort()
    for x in range(len(intlist)):
        if intlist[x] != 0:
            lowlength = intlist[x]
            break
    if cutcount > 0:
        print(cutcount)
