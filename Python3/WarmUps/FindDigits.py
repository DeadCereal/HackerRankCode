numcases = int(input())
for _ in range(numcases):
    numin = input()
    N = int(numin)
    count = 0
    for x in numin:
        if int(x) != 0:
            if N % int(x)==0:
                count += 1
    print(count)
