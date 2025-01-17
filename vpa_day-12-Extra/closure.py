def fun1(x):
    def fun2(y):
        return x + y  
    return fun2  

closure = fun1(10)
print(closure(5))

def fun3(name):
    def fun4(age):
        return f'my name is {name} and age is {age}'
    return fun4

closure = fun3("abc")
print(closure(23))