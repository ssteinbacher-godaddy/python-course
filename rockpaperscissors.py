import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('do you want rock, paper, or scissors? ')
print('computer chose: ' + computer_choice)

if computer_choice == user_choice:
    print("tie")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("you win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("you win")
elif user_choice  == 'scissors' and computer_choice == 'rock':
    print("you win")
else:
    print("computer wins")
