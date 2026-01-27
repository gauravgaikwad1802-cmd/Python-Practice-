n=int(input(""))
orignal=n
rev=0
while n>0:
   digit=n%10
   rev=rev*10+digit
   n=n//10
if orignal==rev:
   print("the given Number is Palindrome")
else:
   print("the given number is Not Palindrome")