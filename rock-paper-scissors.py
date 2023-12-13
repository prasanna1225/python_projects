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

list_of_rps=[rock, paper, scissors ]
#print(list_of_rps)
user_choice=int(input("0 for Rock, 1 for paper, 2 for scissors\n"))
print(list_of_rps[user_choice])
comp_choice=random.randint(0,2)
print(list_of_rps[comp_choice])
if( user_choice >=3 or  user_choice < 0):
    print("please choose valid number to play")
elif(user_choice==0 and comp_choice==2):
    print("YOU WIN!")
elif(comp_choice==0 and user_choice==2):
    print("YOU LOSE!")
elif(user_choice==2 and comp_choice==1):
    print("YOU WIN!")
elif(comp_choice==2 and user_choice==1):
    print("YOU LOSE!")
elif(user_choice==1 and comp_choice==0):
    print("YOU WIN!")
elif(comp_choice==1 and user_choice==0):
    print("YOU LOSE!")
elif(user_choice==comp_choice):
    print("It's Draw!")
    
