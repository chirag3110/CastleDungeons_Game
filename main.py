n=int(input())
l=list(map(int,input().split()))
print(l)
d=dict()
for i in l:
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1
c=0
for i in d.values():
  c=c+int(i/2)
print(c)
