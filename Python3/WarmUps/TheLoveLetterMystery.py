T=int(input())
for _ in range(0,T):
    word=input()
    listword=list(word)
    y=len(word)-1
    count=0
    x=0
    while x < y:
        if listword[x]>listword[y]:
            while listword[x] != listword[y]:
                listword[x]=chr(ord(listword[x])-1)
                count=count+1
        elif listword[y]>listword[x]:
            while listword[x] != listword[y]:
                listword[y]=chr(ord(listword[y])-1)
                count=count+1
        y=y-1
        x=x+1
    print(count)
            
