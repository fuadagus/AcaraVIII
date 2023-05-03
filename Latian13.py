strPembatas = "========================================="
strAlenea = "\n"

#File function
print(strPembatas, strAlenea)
print("File Function")
print("No. 1")
print("\n")

f=open("test.txt", "w")
f.write("Hello, world!")
f.close()
print("File written")

print(strPembatas, strAlenea)
print("No. 2")
print("\n")

f=open("test.txt", "r")
for line in f:
    print(line)
    print(line, end="")
f.close()

print(strPembatas, strAlenea)
print("No. 3")
print("\n")

f=open("test.txt", "a")
f.write("\nHello, world again!")
f.write("\nHello, Agus!")
f.close()

print(strPembatas, strAlenea)
print("No. 4")  
print("\n")

inputFile=open("test.txt", "r")
outputFile=open("test2.txt", "w")
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()

print(strPembatas, strAlenea)
print("No. 5")
print("\n")

inputFile=open("test.txt", "r")
outputFile=open("test2.txt", "w")
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()

print(strPembatas, strAlenea)
print("No. 6")
print("\n")

inputFile=open("test.jpg", "rb")
outputFile=open("test2.jpg", "wb")
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()

print(strPembatas, strAlenea)
