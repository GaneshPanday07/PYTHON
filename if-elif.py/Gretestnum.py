#find the greter num between 3 num 
a = int(input("enter the 1st num= "))
b = int(input("enter the 2nd num= "))
c = int(input("enter the 3rd num= "))

if(a>b and a>c):
    print("A is greter num", a)
elif(b>c):
    print("B is greter num", b)
else:
    print("C is greter num", c)