import random

def get_input():
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides on each die: "))
    return num_dice, num_sides

def roll_dice(num_dice, num_sides):
    return [random.randint(1, num_sides) for _ in range(num_dice)]


def dice_roller():
    num_dice, num_sides = get_input()
    rolls = roll_dice(num_dice, num_sides)
    display_results(rolls)

def display_results(rolls):
    print("Results: ", rolls)

dice_roller()