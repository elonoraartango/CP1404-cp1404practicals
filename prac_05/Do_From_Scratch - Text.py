word = input("Text:")
word_list = word.split()
wordcount = {}

for word in word_list:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1

mydict = {'': '', }
for key in sorted(mydict.iterkeys()):
    print("" % (key, mydict[key]))

def pretty_print(wordcount):
    value_key = []
    for val, key in wordcount.items():
        value_key.append((key, val))

        value_key.sort()

    for val, key in value_key:
        print('{:12s}  {:<3d}'.format(key, val))

pretty_print(wordcount)



