file = open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file1 = open('Codingal.txt','a')
file1.write("Hai! I am a girl")
file1.close()
