import time
arr=[]
file1=open("test.txt","r")
out=file1.readlines()
for i in out:
    arr.extend([int(i) for i in i.split()])


start_time = time.time()


arr.sort()
print(arr)

print("--- %s seconds ---" % (time.time() - start_time))
