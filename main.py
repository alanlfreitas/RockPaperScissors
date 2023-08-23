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

#states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia", "New York", "North Carolina","Rhode Island", "Vermont", "Kentucky", "Tenessee", "Ohio","Louisiana", "Indiana", "Mississipi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#states_of_america[1] = "Pencilvania"

#states_of_america.append("Newland1") #append adds only one item in the end

#states_of_america.extend(["Newland2", "Newland3"]) #extend adds a list to the end of the original list

#print(states_of_america)

#################### Random choice of string ##################
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#name = random.choice(names)
#print(f"{name} vai pagar a conta hoje.")
len_names = len(names)
random_names = random.randint(0,len_names -1)
pay = names[random_names] 
print(pay + " is going to buy the meal today!")

