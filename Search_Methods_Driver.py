# Jackson J.
# 4.10.2020
# This file is the Driver for the methods in the Search_Method file

from Search_Methods import *
from random import randint
from time import sleep
lists = []

# Eye candy for the user:
input('*PRESS ENTER TO START*')
sleep(.5)

name = input("\nHello there user, what is your name?"
             "\n>>>").title()
sleep(.5)
print(f'Oh, it\'s you. I remember you, {name}, nice to see you again.')
sleep(1.5)
print("\nYou know what, I have a cool code for you to look at today."
      "\nIt uses a bit of recursion and some iterative methods."
      "\nI heard you were interested in that.")

sleep(3)
choice = input("\nIn order to get started though, you must type start."
               "\n>>>").title()

while choice != 'Start':
    choice = input('\nAwe come on, do you not want to experience to code?'
                   '\nType "start" please.'
                   '\n>>>').title()

sleep(.5)
print("\nGood to hear!"
      "\nNow, let me load the program.")

# Suppose to add characteristic, but at the expense of the users time
a = 1
for i in range(0, 4):
    print("." * a)
    a += 1
    sleep(1)
print("_" * 100)

# This is loop that runs the whole program
while choice == 'Start':
    sleep(1)
    print("\n\nEnter the NUMBER  or  the FIRST LETTER of the desired sort method.")
    menu = 'Continue'
    while menu == 'Continue':

        # I added a loop to ensure the user picked one of the choices
        # Then i set menu equal to a single number so i could write the import statements easier later on in the code
        while menu:
            sleep(1)
            menu = input('\n\n   -MENU-'
                         '\n1. BUBBLE'
                         '\n2. INSERTION'
                         '\n3. SELECTION'
                         '\n4. MERGE'
                         '\n5. QUICK'
                         '\n6. Exit'
                         '\n>>>').title()

            if menu == '1' or menu == 'B':
                menu = 1
                break

            elif menu == '2' or menu == 'I':
                menu = 2
                break

            elif menu == '3' or menu == 'S':
                menu = 3
                break

            elif menu == '4' or menu == 'M':
                menu = 4
                break

            elif menu == '5' or menu == 'Q':
                menu = 5
                break

            elif menu == '6' or menu == 'E':
                print('\nThanks for playing!'
                      f'\nBye {name}.')
                exit()

            else:
                print('Again please.')

        # I have a variable that asks how many values the user wants to add to the list.
        # If the user tries to enter a string of a float, they will be butt hurt because they will fail.. unless they only press enter
        # The try statement is what allow the value checking
        amount = input('\nHow many random numbers would you like me to sort?'
                       '\nDon\'t go too crazy...'
                       '\n>>>')
        while amount:
            try:
                amount = int(amount)
                break
            except ValueError:
                amount = input("Can you enter a whole number?"
                               "\n>>>")

        # This loop add the random numbers to the list.
        # The amount of values added is determined on the previous piece of code
        for i in range(0, amount):
            lists.append(randint(1, 100000))
        print("\nThe numbers in the list are:\n", lists,)
        sleep(1.5)
        print("\nSorted, the list looks like this:")
        # The following if statements will call the method the user picked and sort the list using that method.
        # You can see menu == 1 and so on. Earlier i set menu = to a single number whilst representing the method called with one number, if that makes sense
        if menu == 1:
            print(Bubble_Sort(lists))

        elif menu == 2:
            print(Insertion_Sort(lists))

        elif menu == 3:
            print(Selection_Sort(lists))

        elif menu == 4:
            print(Merge_Sort(lists))

        elif menu == 5:
            print(Quick_Sort(lists))

        print('\nBam!')

        sleep(.1)
        print('\nWas\'t that cool?'
              '\nI\'m going to take you back to the menu now.'
              '\nThere, you can try again, or you can exit the program.')

        lists.clear()  # The user might want to use try other methods
        input('\n*PRESS ENTER*')
        sleep(1.5)  # Yes this is here on purpose
        print("_" * 100)
