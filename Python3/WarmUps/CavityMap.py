N = int(input())
topmap = []
for _ in range(N):
    stringin = input()
    row=[]
    for ch in stringin:
        row.append(ch)
    topmap.append(row)

for x in range(1,N-1):
    for y in range(1,N-1):
        value = int(topmap[x][y])
        if topmap[x-1][y] != "X" and value > int(topmap[x-1][y]):
            if topmap[x+1][y] != "X" and value > int(topmap[x+1][y]):
                if topmap[x][y-1] != "X" and value > int(topmap[x][y-1]):
                    if topmap[x][y+1] != "X" and value > int(topmap[x][y+1]):
                        topmap[x][y]="X"

for x in topmap:
    for y in x:
        print(y,end="")
    print("")
