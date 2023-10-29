

number = int(input("enter the number : "))
print(number)

factorial = 1

if number < 0:
    print("factorials are not defined for the negative numbers")

elif number == 0:
    print("the factorial of 0 is 1")

else :
    while (number>0) :
        factorial *= number
        number -= 1

    
print(" the factorial of given number is ",factorial)