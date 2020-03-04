f = open('inputFile.txt','r')
passFile = open('PassFile.txt','w')
failFile = open('FailFile.txt','w')
#count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
        #print(line)
    #print(str(count) + line)
    #count = count + 1
#print(f.read())
f.close()
passFile.close()
failFile.close()
