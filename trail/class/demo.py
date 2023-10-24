
print("demo \n")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Person2:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)



p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)

p2 = Person2("John", 36)
p2.myfunc()