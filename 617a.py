for z in range(int(input())):
	n=int(input())
	arr=[int(i) for i in input().split()]
	if sum(arr)%2!=0:
		print("YES")
		continue
	else:
		check=False
		for i in arr:
			if i%2!=0:
				check=True
				break
		if check==False:
			print("NO")
			continue
		elif check==True:
			newcheck=False
			for i in arr:
				if i%2==0:
					newcheck=True
					break
			if newcheck:
				print("YES")
			else:
				print("NO")