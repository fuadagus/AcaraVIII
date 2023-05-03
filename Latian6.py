strPembatas = "========================================="
strAlenea = "\n"

#condition
print("Condition")
print("No. 1")
print("\n")

userInput = input("Enter your password: ")
if userInput == "secret":
    print("You have access!")
    print("it's a secret to everybody")
elif userInput == "something else":
    print("Nope, sorry!")
    print("Goodbye")
else:
    userInput != "secret" or "something else"
    print("Access denied!")

print(strPembatas, strAlenea)
print("No. 2")
print("\n")
