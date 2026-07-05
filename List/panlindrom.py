list1 = [1,2,3,2,1]

copy = list.copy(list1)
copy.reverse()


if(copy == list1):
    print("palindrome")
else:
    print("Not palindrome")