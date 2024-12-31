#Accessing a global variable inside a function
#Note that Global variables are set before the function
# whiles local variables are set within the variable
x = 10
#writing my function
def print_global():
    print("The value stored in the global variable is:", x)
print_global()      #end the function by calling the function

#Writing the variable in the function mostly not reusable
def print_global(x=50):
    print("The new value of x is:", x)
print_global()

#Reusable functions
def print_global(a,b):
    result= a + b
    print("The value of a and b is:", result)
print_global(5, 6)

#Local variables:
def my_local_variable():
    x= 10 #local variable
    print(x)
my_local_variable()
