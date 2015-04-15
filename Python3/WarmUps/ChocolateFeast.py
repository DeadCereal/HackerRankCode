T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    answer = int(int(N)/int(C))
    wrappercount = answer
    while wrappercount >= int(M):
        wrapperbuy = int(wrappercount/int(M))
        answer+=wrapperbuy
        wrappercount = (wrappercount - int(int(M)*wrapperbuy)) + wrapperbuy
        
    print(answer)
