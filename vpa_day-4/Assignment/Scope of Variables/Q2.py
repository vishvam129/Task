# Demonstrate the behavior of nonlocal by creating a nested function that manipulates a 
# variable in the enclosing scope.

def fun():
    a=0
    def fun1():
        b=1
        print(a)
        print(b)
    fun1()

fun()
# a has local scope for fun1 but b has no local scope for fun
# a has called enclosing scope