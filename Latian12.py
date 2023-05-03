strPembatas = "========================================="
strAlenea = "\n"


#Import Module
print(strPembatas, strAlenea)
print("Import Module")
print("No .1")
print("\n")

import prime
x=input("Please enter a number: ")
x=int(x)
answer=prime.checkIfPrime(x)
print(answer)

