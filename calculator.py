print("-----CALCULATOR-----");
print(" 1 --> Addition \n 2 --> Diffrence \n 3 --> Multiplication \n 4 --> Division")
a=int(input("Enter a number --------->"))
b=int(input("Enter another number --->"))
c=int(input("----ENTER YOUR CHOICE----"))
if (c==1):
	s=a+b
	print(a,"+",b,"=",s)
elif(c==2):
	s=a-b
	print(a,"-",b,"=",s)
elif(c==3):
	s=a*b
	print(a,"x",b,"=",s)
else:
	s=a/b
	print(a,"/",b,"=",s)			
	


