# Types of Function Arguments
#               - Default arguments
#               - Keyword arguments
#               - Positional arguments
#               - Arbitrary Positional Arguments in Python
    #                   - Arbitrary Keyword Arguments in Python


def fun_default(gm="Good Morning"):
    print("THe keyword is :- ",gm)
fun_default()


def fun_keyword(sm,gm):
    print("This is default argyment :- ",sm + gm)
fun_keyword(gm="Goodmorning",sm="Hello")

def fun_positional(name,position):
    print(f"The Name is {name} and the position is {position}")
fun_positional("Abc","Ceo") #Right 
fun_positional("Ceo","Abc") #Wrong

def fun_Arbitrary_positionl(name,*args):
    print("The name is ",name, "and other details is ",args)
fun_Arbitrary_positionl("Abc","hi i am abc"," I am ceo")
fun_Arbitrary_positionl("hi i am abc"," I am ceo","Abc")

def fun_Arbitrary_keyword(name,**kwargs):
    print("MY name is ",name ,"and other details is ",kwargs)
fun_Arbitrary_keyword(name="abc",position="ceo",hobbies="cricket")
