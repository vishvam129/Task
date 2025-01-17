
# Python exec() Syntax


#     exec(object[, globals[, locals]]) 

#     Parameters:


#         object: As already said this can be a string or object code

#         globals: This can be a dictionary and the parameter is optional

#         locals: This can be a mapping object and is also optional




prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

from math import *
exec("print(dir())")

# factorial() will be executed
from math import *
exec("print(fact(5))", {"fact":factorial})
