
STATE_NAMES = {"QLD": "Queensland", "qld": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
               "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA" : "South Australia"}

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
