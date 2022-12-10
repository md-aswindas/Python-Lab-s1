print("***MULTIPLICATION TABLE***")
n=int(input("enter the number : "))
m=int(input("enter the limit : "))
for i in range(1,m+1,1):
	s=n*i
	print(i,"x",n,"=",s)
