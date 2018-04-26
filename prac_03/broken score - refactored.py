
def level_scored(score):
    while score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    else:
        if score > 50:
            print("Passable")
        if score > 90:
            print("Excellent")
    if score < 50:
        print("Bad")
    return score


score = float(input("Enter score: "))
print(level_scored(score))