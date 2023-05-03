strPembatas = "========================================="
strAlenea = "\n"

# Def Function
print(strPembatas, strAlenea)
print("Def Function")
print("No. 1")
print("\n")

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck % x == 0):
            return False
    return True
answer = checkIfPrime(13)
print(answer)


print(strPembatas, strAlenea)
print("No. 2")
print("\n")

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck % x == 0):
            return False
    return True
x=int(input("Please enter a number: "))
x=int(x)
answer=checkIfPrime(x)
print(answer)

print(strPembatas, strAlenea)
