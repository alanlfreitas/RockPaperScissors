import random

#random_interger = random.randint(1,10)
#print(random_interger)

#random_float = random.random() * 5
#print(random_float)

#love_score = random.randint(1,100)
#print(f"Your love score is {love_score}.")

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
#import random

#################### Flip a coin ####################
#flipcoin = random.randint(1,2)
#if flipcoin == 1:
#    print("Heads")
#else:
#    print("Tails")

# states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia", "New York", "North Carolina","Rhode Island", "Vermont", "Kentucky", "Tenessee", "Ohio","Louisiana", "Indiana", "Mississipi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_america[1] = "Pencilvania"

# states_of_america.append("Newland1") #append adds only one item in the end

# states_of_america.extend(["Newland2", "Newland3"]) #extend adds a list to the end of the original list

# print(len(states_of_america))

# print(states_of_america)

#################### Random choice of string ##################
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# #name = random.choice(names)
# #print(f"{name} vai pagar a conta hoje.")
# len_names = len(names)
# random_names = random.randint(0,len_names -1)
# pay = names[random_names] 
# print(pay + " is going to buy the meal today!")

#Lists within lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# # print(dirty_dozen) 
# print(dirty_dozen[1])

from os import system as sys


# def TreasureMap():
#   # -------------------- TREASURE MAP -------------------- #
#   # 🚨 Don't change the code below 👇
#   row1 = ["⬜️","️⬜️","️⬜️"]
#   row2 = ["⬜️","⬜️","️⬜️"]
#   row3 = ["⬜️️","⬜️️","⬜️️"]
#   map = [row1, row2, row3]
#   print(f"{row1}\n{row2}\n{row3}")
#   position = input("Where do you want to put the treasure? ")
#   # 🚨 Don't change the code above 👆

#   #Write your code below this row 👇
#   horizontal = int(position[0])
#   vertical = int(position[1])
#   row = map[vertical - 1]
#   row[horizontal - 1] = "X"

#   #Write your code above this row 👆

#   # 🚨 Don't change the code below 👇
#   print(f"{row1}\n{row2}\n{row3}")
# TreasureMap()

#def RockPaperScissors():
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user = int(input("What do you choose? 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n"))
if user >= 3 or user < 0:
  print("Invalid number. You lose")
else:
  print("You chose:")
  print(images[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(images[computer])

#if user >= 3 or user < 0:
  #print("Invalid number. You lose!")

if user == 0 and computer == 2:
  print("You win!")

elif computer == 0 and user == 2:
  print("You lose!")

elif computer > user:
  print("You lose!")

elif user > computer:
  print("You win!")

elif computer == user:
  print("It's a draw!")