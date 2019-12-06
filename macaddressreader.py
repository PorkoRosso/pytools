import uuid 

#The usage parameters for the program are written into the readme
f = open("README.txt","r")
#Read the contents 
contents = f.read().split('\n')
#If the MAC matches and it has been used before continue you with the program
if contents[0] == hex(uuid.getnode()) and contents[1] == '1':
	print('thanks for playing by the rules')
#If the program has been used before and on a different mac close connections quit program
elif contents[0] != hex(uuid.getnode()) and contents[1] == '1':
	print('ur dead one computer only')
	f.close()
	quit()
#Else it is first time program use 
else:
	f = open("README.txt","w+")
	f.write(hex(uuid.getnode()))
	f.write('\n1')
	print('Hello ',hex(uuid.getnode()))
	f.close()

print('finished')
f.close()
