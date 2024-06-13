import random
print("""
██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
print("Welcome to the rock paper scissors Game!\n")
help=input("Press Enter to continue or type (help) for the rules:").lower()
x=["help"]
choes=["rock","paper","scissors"]
if help:
  if help in x:
    print("1-Rock wins against scissors\n 2-paper wins against rock\n 3-scissors wins against paper\n")
  else:
    print("invailed choice")
else:
  print("Enter your choice (rock,paper,scissors): \n")
  user_choice=input("Enter your choice: ").lower()
  cp_choice=random.choice(choes)
  if user_choice in choes:
   if (user_choice=="rock" and cp_choice=="scissor") or (user_choice=="paper" and cp_choice=="rock") or (user_choice=="scissors" and cp_choice=="paper"):
    print(f" computer choice is {cp_choice}\n your choice is {user_choice}\n you win")
   elif user_choice==cp_choice:
    print(f" computer choice is {cp_choice}\n your choice is {user_choice}\n it's a tie")
   else:
    print(f" computer choice is {cp_choice}\n your choice is {user_choice}\n you lose")