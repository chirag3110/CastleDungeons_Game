n,m=map(int,input().split())
dic1={}
dic2={}
for _ in range(m):
    arr=input().split()
    if arr[0] in dic1:
        dic1[arr[0]]+=1
    else:
        dic1[arr[0]]=1
    if arr[0] in dic2:
        dic2[arr[0]]+=int(arr[1])
    else:
        dic2[arr[0]]=int(arr[1])
# print(dic1)
# print(dic2)
myteam='BhayanakMaut'

myteamscore=dic1[myteam]
myteampen=dic2[myteam]
dic1.pop(myteam)
dic2.pop(myteam)
above=0
equal=0
penabove=0
equalarr=[]
for i in dic1:
    if dic1[i]>myteamscore:
        above+=1
    if dic1[i]==myteamscore:
        equalarr.append(i)
# print(equalarr)
for i in equalarr:
    if dic2[i]<myteampen:
        penabove+=1
print(above+penabove+1)

