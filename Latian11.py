strPembatas = "========================================="
strAlenea = "\n"

# Variable Scope
print("Variable Scope")
print("No. 1")
print("\n")

message = "Global variable (shares same as local)"
def myFunction():
    print(message)
    message = "Local variable (shares same as global)"
    print("\nInside the function, the message says:", message)
    #call the function
myFunction()
# print the global variable
print("\nOutside the function, the message says:", message)
print(message)

print(strPembatas, strAlenea)
print("No. 2")
print("\n")

message1= "Global variable (shares same as local)"
message2= "variable shares"
def myFunction():
    print("\nInside the function, the message says:", message1)
    #Global variable are accessible inside functions
    print(message1)
    #Declare a local variable
    message2= "Local variable"
    print(message2)
#call the function
myFunction()
print("\nOutside the function, the message says:", message1)
#Global variable are accessible outside functions
print(message1)
#Local variable are not accessible outside functions
print(message2)