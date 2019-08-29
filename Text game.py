# Snake, water , gun game

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t::::: Snake,Water,Gun Game:::::\n \n")
print("Enter s for snake \nEnter w for water \nEnter g for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each. \n ")

    # if user enter s
    if _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("Human wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("Human wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("Human wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}. \n")
        print("computer wins 1 point. \n")
        print(f"computer_point is {computer_point} and your point is {human_point}. \n ")

    else:
        print("you have input wrong. \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over!!!")

if computer_point > human_point:
    print("Computer wins and you loose.")

if computer_point < human_point:
    print("You win and computer loose.")

print(f"your point is {human_point} and computer point is {computer_point}.")



#Output

	::::: Snake,Water,Gun Game:::::
 

Enter s for snake: 
Enter w for water: 
Enter g for gun: 

Snake,Water,Gun:s
Tie Both 0 point to each. 
 
you have input wrong. 

9 is left out of 10. 

Snake,Water,Gun:s
Tie Both 0 point to each. 
 
you have input wrong. 

8 is left out of 10. 

Snake,Water,Gun:s
your guess s and computer guess is w. 

Human wins 1 point. 

computer_point is 0 and your point is 1. 

7 is left out of 10. 

Snake,Water,Gun:s
your guess s and computer guess is g. 

computer wins 1 point 

computer_point is 1 and your point is 1. 
 
6 is left out of 10. 

Snake,Water,Gun:w
Tie Both 0 point to each. 
 
you have input wrong. 

5 is left out of 10. 

Snake,Water,Gun:g
your guess g and computer guess is s. 

Human wins 1 point. 

computer_point is 1 and your point is 2. 

4 is left out of 10. 

Snake,Water,Gun:g
Tie Both 0 point to each. 
 
you have input wrong. 

3 is left out of 10. 

Snake,Water,Gun:w
your guess w and computer guess is s. 

computer wins 1 point. 

computer_point is 2 and your point is 2. 
 
2 is left out of 10. 

Snake,Water,Gun:g
your guess g and computer guess is w. 

computer wins 1 point. 

computer_point is 3 and your point is 2. 
 
1 is left out of 10. 

Snake,Water,Gun:s
your guess s and computer guess is w. 

Human wins 1 point. 

computer_point is 3 and your point is 3. 

0 is left out of 10. 

Game over!!!
your point is 3 and computer point is 3.




