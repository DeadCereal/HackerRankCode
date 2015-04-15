#!/usr/bin/py
# Head ends here
def lonelyinteger(intlist):
    answer = 0
    for key, value in intlist.items():
        if value == 0:
            answer = key
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    intlist = {}
    for x in b:
        if x in intlist:
            intlist[x] += 1
        else:
            intlist[x] = 0
    print(lonelyinteger(intlist))
