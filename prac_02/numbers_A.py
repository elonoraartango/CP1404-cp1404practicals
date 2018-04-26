
infile = open('numbersaa.txt','r')  #name of file that numbers have been read from
Number_1 = int(infile.readline())  #system automatically reads the first line and prints the data in that line
Number_2 = int(infile.readline())   #system automatically reads the first line and prints the data in that line
print(Number_1 + Number_2)  #printing the sum of both numbers in 'number.txt' file
infile.close()  #closes the file


