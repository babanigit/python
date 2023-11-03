
def fun(x):
    z = x + 3

    def fun2(x):

        z = 3 + x
        print(z)

    fun2(z)

print("hello")

fun(2)

print("hello 2")


def funReturn(x):
    
    def funReturn2(x):

        return x
    
    funReturn()
    
    return x

funReturn()