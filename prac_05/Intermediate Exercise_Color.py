print("""
Select a Colour:  
Beige
Blue Violet
Brown
Chocolate
Coral
Dark Golden Rod
Dark Green
Firebrick
Ghost White
""")


COLOUR_CODES = {"ALICE BLUE": "#f0f8ff", "BEIGE": "f5f5dc", "BLUE VIOLET": "#8a2be2","BROWN": "#a52a2a", "CHOCOLATE": "#d2691e", "CORAL": "#ff7f50", "DARK GOLDEN ROD": "#ffb90f", "DARK GREEN": "#006400", "FIREBRICK": "#b22222", "GHOST WHITE": "#f8f8ff"}
# print(STATE_NAMES)

colour = input("Enter Colour: ").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print("The ",colour," colour code is", COLOUR_CODES[colour])
    else:
        print("Invalid Colour name")
    colour = input("Enter Colour: ").upper()
