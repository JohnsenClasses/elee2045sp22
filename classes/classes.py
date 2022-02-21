from MyClass import MyClass

a_myclass = MyClass([1,2,3],[])
another_myclass = MyClass([4,5,6])
print(type(a_myclass))

print(id(a_myclass),id(another_myclass))
print(a_myclass.a_list,another_myclass.a_list)

