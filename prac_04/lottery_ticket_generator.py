import random


def main():

    quick_picks = int(input("How many quick picks?"))

    for i in range(1, quick_picks + 1):
        print(random.sample(range(0, 46), 6))


main()
