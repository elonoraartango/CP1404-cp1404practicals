
def celcius_to_fahrenheit(celcius):
    return celsius * .8 + 32.0


def fahrenheit_to_celcius(fahrenheit):
    return celsius * 9.0 / 5 + 32


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        print("Result: {:.2f} F".format(celcius_to_fahrenheit(choice)))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        print("Result: {:.2f}  C".format(fahrenheit_to_celcius(choice)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")