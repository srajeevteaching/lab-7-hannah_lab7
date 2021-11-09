# Hannah Hodges
# CS151, Dr. Rajeev
# Lab 7
# 11/09/2021
# import random for dice roll between 1 and 6
import random


# main function to run the program
def main():
    result_sum = []
    num = int(input("Enter number of rolls:"))
    for i in range(num):
        result_sum.append(sum)


# function to get a certain number of rolls
def get_number_of_rolls():
    input("")
    if str.isdigit():
        print("Error. Enter an integer")
    else:
        return input()


# function for dice rolls sums
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    return sum


# histogram is created so a list of sum results can be printed 
def create_histogram(num):
    for i in num:
        rolls = num
        print((sum, '*'))


main()
