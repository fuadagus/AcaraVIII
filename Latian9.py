strPembatas = "========================================="
strAlenea = "\n"

#whileLoop
print("While Loop")
print("No. 1")
print("\n")

counter = 30
while counter > 0:
    print(counter)
    counter -= 1
print("Blast off!")

print(strPembatas, strAlenea)
print("No. 2")
print("\n")
j = 0
for i in range(5):
    j += 1
    print(j)
    print("i =", i, "j =", j)
    if (i == 3):
        break

print(strPembatas, strAlenea)
print("No. 3")
print("\n")

j = 0
for i in range(5):
    j = j + 1
    print('\ni =', i, 'j =', j)
    if (i == 3):
        continue
    print('I will be skipped over if i=3')

print(strPembatas, strAlenea)
print("No. 4")
print("\n")

try:
    answer = 12/0
    print(answer)
except:
    print("An error occurred")

print(strPembatas, strAlenea)
print("No. 5")
print("\n")

try:
    x=int(input("Please enter a number as x: "))
    y=int(input("Please enter a number as y: "))
    answer=int(x)/int(y)
    print(answer)
except:
    print("An error occurred")

try:
    x=int(input("Please enter a number as x: "))
    y=int(input("Please enter a number as y: "))
    answer=float(x)/(y)
    print(answer)
except:
    print("An error occurred")
