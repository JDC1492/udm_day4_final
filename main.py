import random

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

player_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.")
plyr_int=int(player_choice)

if plyr_int == 0:
  print(rock)
elif plyr_int == 1:
  print(paper)
elif plyr_int == 2:
  print(scissors)

cpu_choice = random.randint(0, 2)
print("CPU chooses: ")
if cpu_choice == 0:
  print("Rock"+ rock)
elif cpu_choice == 1:
  print("Paper"+ paper)
elif cpu_choice == 2:
  print("Scissors"+ scissors)

if plyr_int == cpu_choice:
  print("Alas...Another Battle to Fight.")
elif (plyr_int == 0 and cpu_choice == 1):
  print("You Lose")
elif (plyr_int == 1 and cpu_choice == 2):
  print("You Lose")
elif (plyr_int == 2 and cpu_choice == 0):
  print("You Lose")
else:
  print("You Win!")
# successfully solved