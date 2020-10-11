n,m=map(int,input().split())
arr=[int(i) for i in input().split()]
res=m%n
ans=arr[res:]+arr[:res]
# print(ans)
for i in ans:
	print(i,end=' ')
