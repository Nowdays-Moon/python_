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

#Write your code below this line 👇

my_choice = int(input("What Do you choose? Type 0 for rock, 1 for Paper or 2 for Siccors\n"))

if my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
elif my_choice == 2:
  print(scissors)
else:
  print("You inputted wrong number")

import random
computer_choose = random.randint(0,2)
print(computer_choose)

if computer_choose == 0:
  print(rock)
elif computer_choose == 1:
  print(paper)
elif computer_choose ==2:
  print(scissors)

if computer_choose == 1:
  if my_choice == 0:
    print("You lose")
  elif my_choice == 1:
    print('Draw')
  elif my_choice == 2:
    print("You Win")
elif computer_choose == 2:
  if my_choice == 0:
    print("You Win")
  elif my_choice == 1:
    print('You Lose')
  elif my_choice == 2:
    print("Draw")

elif computer_choose == 0:
  if my_choice == 0:
    print("Draw")
  elif my_choice == 1:
    print('You win')
  elif my_choice == 2:
    print("You Lose")
