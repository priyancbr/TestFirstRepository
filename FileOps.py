myf = open('myfile.txt')
print(myf.read())
print(myf.read())
print(myf.seek(0))
print(myf.readlines())
print(myf.seek(0))
print(myf.readlines())
print(myf.seek(0))
print(myf.readline())
myf.close()
myf = open('myfile.txt',mode='r+')
myf.write('\nWrote a line')
print(myf.read())


MyFile = open('test.txt', mode ='w')
MyFile.write("THis is written using code")
MyFile.close()
MyFile = open('test.txt', mode = 'r')
print(MyFile.read())
MyFile.close()
MyFile = open('test.txt', mode = 'a')
MyFile.write("Hello, AGain wrote using code")
MyFile.close()
