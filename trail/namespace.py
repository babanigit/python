

var1 = 5

def some_func():
    var2 = 6
    print(var2)
    
    def some_inner_func(x):
        global var1
        var3 = 7 + var1 + x
        print(var3)


    some_inner_func(34)
    some_inner_func(45)

    return "return"
        
print(var1)
some_func()

def some_func(trail):
    print("hello")
    

    def some_inner_func(trail):
        print("hello")
        return trail + 69


    print(some_inner_func(100))
    
trail = some_func(69)
print(trail)
