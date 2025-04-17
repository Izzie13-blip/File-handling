f = open('Codingal.txt','r')
print(f)
print(f.read())
f.close()

f1 = open('Codingal.txt','w')
w1 = f1.write('Hello World')
#print(w1)
f1.close()

f2 = open('Codingal.txt','a')
w2 =f2.write('Its a new day')
#print(w1)
f2.close()
