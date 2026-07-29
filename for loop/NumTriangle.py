for i in range(1,7):
    for j in range(1,i,+1):
        print(j,end=" ")
    print()


for i in range(1,7):
    for j in range(1,i,+1):
        print(5,end=" ")
    print()


num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()