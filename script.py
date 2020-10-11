def happy(n):
    while(n!=1):
        for i in str(n):
            n+=int(i)**2
    return True
    
for i in range(1,100):
    if happy(i):
        print(i, "True")