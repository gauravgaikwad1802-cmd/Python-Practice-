a=int(input(""))
temp=a
b=len(str(a))
s=0
while temp > 0:
    d=  temp%10
    s=s+d**b
    temp=temp//10
if s == a:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")\
    


