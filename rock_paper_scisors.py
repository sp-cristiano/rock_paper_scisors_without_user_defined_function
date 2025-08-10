'''

Rock, Paper, Scissors Game

This is a simple rock paper scissors game.
There are better ways of writing this code but this is just for practice.
In this code we use the random module to generate the computer's choice
I decided not to use a user defined function because i want you to see how things work without using a user defined function.

'''
import random

counter = 0
limit = 5
player_point = 0
computer_point = 0
player_choice_in_choices_count = 0

star = '********************************************************'  # 56 starts
welcome = 'Welcome to Rock, Paper, Scissors Game'
print('')
print(star)
print(welcome.center(56).upper())
print(star)
print('')
print('Rules of the game'.center(56))
print('Rock beats scissors, scissors beat paper, paper beats rock')
print('')
print('')

choices = ['rock', 'paper', 'scissors']

while counter < limit:
    try:
        player_choice = input('Enter your choice: ').lower()
        computer_choice = random.choice(choices)

        if player_choice not in choices:
            print('Invalid input')
            counter += 1
            remaining_trials = limit - counter
            if remaining_trials == 0:
                print('Game Over')
                if player_choice_in_choices_count == 0:
                    print('You lossed all your trials')
                    print('You lose the game')
                    print(f'Your total point is: {player_point}')
                else:

                    if player_point > computer_point:
                        print('You won the game')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                    elif player_point == computer_point:
                        print('This game ended in a Draw')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                    else:
                        print('You lose this game')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                break
            else:
                print(f'Player point: {player_point}')
                print(f'Computer point: {computer_point}')
                print(f'You have {remaining_trials} trials left')
                print('')
                print('')
                continue
        else:
            if player_choice == computer_choice:
                print(f'You chose {player_choice}')
                print(f'Computer chose {computer_choice}')
                print('This is a Draw')
                player_choice_in_choices_count += 1
                print('')
                print('')
            elif player_choice == 'rock' and computer_choice == 'scissors':
                print(f'You chose {player_choice}')
                print(f'Computer chose {computer_choice}')
                print('You win')
                player_point += 1
                player_choice_in_choices_count += 1
                print(f'Player point: {player_point}')
                print(f'Computer point: {computer_point}')
                print('')
                print('')
            elif player_choice == 'scissors' and computer_choice == 'paper':
                print(f'You chose {player_choice}')
                print(f'Computer chose {computer_choice}')
                print('You win')
                player_point += 1
                player_choice_in_choices_count += 1
                print(f'Player point: {player_point}')
                print(f'Computer point: {computer_point}')
                print('')
                print('')
            elif player_choice == 'paper' and computer_choice == 'rock':
                print(f'You chose {player_choice}')
                print(f'Computer chose {computer_choice}')
                print('You win')
                player_point += 1
                player_choice_in_choices_count += 1
                print(f'Player point: {player_point}')
                print(f'Computer point: {computer_point}')
                print('')
                print('')
            else:
                print(f'You chose {player_choice}')
                print(f'Computer chose {computer_choice}')
                print('You lose')
                computer_point += 1
                player_choice_in_choices_count += 1
                print('')
                counter += 1
                remaining_trials = limit - counter

                if remaining_trials == 0:
                    print('Game Over')
                    if player_point > computer_point:
                        print('You won the game')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                    elif player_point == computer_point:
                        print('This game ended in a Draw')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                    else:
                        print('You lose this game')
                        print(f'Your total point is: {player_point}')
                        print(f'Computer total point is: {computer_point}')
                    break
                else:
                    print(f'Player point: {player_point}')
                    print(f'Computer point: {computer_point}')
                    print(f'You have {remaining_trials} trials left')
                    print('')
                    print('')
                    continue
    except:
        print('Invalid input')
        counter += 1
        remaining_trials = limit - counter
        print(f'You have {remaining_trials} trials left')
        print('')
        print('')
        continue
