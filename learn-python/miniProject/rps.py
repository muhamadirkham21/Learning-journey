import random

def get_choices():
    options = ['rock', 'paper', 'scissor']

    player_choice = input('Enter your choice (Rock, Paper, Scissor)').lower()
    computer_choice = random.choice(options)
    choices = {'player': player_choice,
               'computer': computer_choice
               }
    return choices

def check_win(player, computer):
    print(f'You Chose {player}, and Computer chose {computer}')

    if player == computer:
        return 'Draw'
    elif player == 'rock':
        if computer == 'paper':
            return 'you lose'
        else:
            return 'you win'
    elif player == 'paper':
        if computer == 'rock':
            return 'you win'
        else:
            return 'you lose'
    elif player == 'scissor':
        if computer == 'paper':
            return 'you win'
        else:
            return 'you lose'

choises = get_choices()
result = check_win(choises['player'], choises['computer'])
print(result)
