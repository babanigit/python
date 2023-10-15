


def fun(x):
    z = x + 3

    def fun2(x):

        z = 3 + x
        print(z)

    fun2(z)

fun(2)