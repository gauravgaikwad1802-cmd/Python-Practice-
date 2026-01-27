n=int(input(""))
for x in range(2,n+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end="")