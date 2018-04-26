###THE BELOW PROGRAM WILL ALLOW ANY AMOUNT OF NUMBERS TO BE ENTERED AND THE SUM OF ALL NUMBERS ARE PRINTED###

infile = open('numbersaa.txt', 'r')  #name of file that numbers have been read from
total = 0
for digit in infile:
    number = int(digit)
    total += number #adding totals and sum of numbers
print(total)   #prints the total of all numbers summed up
infile.close()  #closes the file
