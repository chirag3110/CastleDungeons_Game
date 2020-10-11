file=open('testcase.txt','r')
file2=open('answer.txt','w')
for i in file:
    n=int(i)
    arr=[]
    for i in range(1,n+1):
        if i%2==0:
            arr.append(i)
    # print(arr)
    check=False
    while(True):
        n=n/2
        if n%2!=0:
            check=True
        for i in range(len(arr)):
            arr[i]=arr[i]/2
        for i in arr:
            if i%2!=0:
                arr.remove(i)
        # print(n)
        # print(arr)
        if check:
            break
    # print(n," over")
    # print(arr, " over")
    print(len(arr))
    file2.write(str(len(arr))+'\n')