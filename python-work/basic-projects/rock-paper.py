import random 

def play():
    user = input("What's your choice? 'R' for Rock, 'P' for Paper, 'S' for scissors \n")
    computer = random.choice(['R', 'P', 'S'])
    
    if user == computer:
        return 'tie'
    
    if is_win(user, computer):
        return 'You Won!'
    if is_win(computer, user):
        return 'You Lost!'

def is_win(player, computer):
    # return true if the player wins
    if (player == 'r'and computer == 's') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        return True
    
print(play())




