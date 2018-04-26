

infile=open('name.txt','r') #name of file that name has been previously saved to
name = infile.read() #'name'(variable) is found and read
print("Your name is:", name)  #asking user for input / data is being taken from file on previous input
infile.close() #closes the file

