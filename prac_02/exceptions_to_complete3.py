finished = False
result = 0
while not finished:
     try:
        result = int(input("Please enter a valid integer: "))
        finished = True
     except ValueError:
        print("This is not a valid number")
print("Valid result is:", result)


"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

#finished = False
#result = 0
#while not finished:
#    try:
        # TODO: this line
        # TODO: this line
#        pass
#    except:# TODO - add something after except
#        print("Please enter a valid integer.")
#print("Valid result is:", result)

