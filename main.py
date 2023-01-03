import random

rock = '''
✊
'''

paper = '''
🖐
'''

scissors = '''
✌️
'''

emoji = [rock, paper, scissors]

player = int(input("0 for rock, 1 for paper, 2 for scissors.\n"))
if player >= 3 or player < 0:
    print("invalid number, you lose!")
else:
    print(emoji[player])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(emoji[computer])

    if player == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and player == 2:
        print("You lose.")
    elif computer > player:
        print("You lose.")
    elif player > computer:
        print("You win!")
    elif computer == player:
        print("It's a draw.")