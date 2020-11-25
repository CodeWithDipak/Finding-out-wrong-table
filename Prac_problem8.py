'''
Author - CodeWithDipak
Date - 8 nov 2020
purpose - Practice Purpose
'''
'''
Rohan is a fraud and he is creating a wrong table of a number.
And distribute among the class during exam period. I catch his fraud and make a program to find the wrong number
in his table and print it's index.
'''




import random
def rohan_multiplication(n):
    table = [n*i for i in range(1, 11)]
    index = random.randint(0, 9)
    table[index] = table[index] + random.randint(0, 9)
    return table


def is_correct(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i
    return None


if __name__ == '__main__':
    num = int(input("Enter the number:\n"))
    my_table = rohan_multiplication(num)
    print(my_table)
    wrong_index = is_correct(my_table, num)
    print(f"The number is wrong at index {wrong_index}.")
