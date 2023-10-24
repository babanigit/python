

a,b,c = 3,4,5
maximum = max(a,b,c)

print(maximum)
print('aniket','panchal','tiger',sep=':')


# formatting 
print("hello {} there {} \n" .format('greek','greeks'))

if a != b:
    if a>b:
        print("a is bigger then b")
    else:
        print("b is bigger")

else:
    print("both are equal")


print("both are equal" if b==c else "b is larger" if b>c else "c is smaller")
