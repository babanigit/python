

num = int (input("enter number : "))
if  (not (num%3 == 0 or num% 4 == 0)):
    print( num, "is not divisible by either 3 or 4")

else:
    print("yes it is divisible by 3 or 4")

num2 = int(input("enter the number : "))
for i in range ( 1, num2):
    if (i%9==0) and (i%5!=0):
        print(str(i))