# Write your code here
import random

name = input("Enter your name: ")
print(f'Hello, {name}')

rating_file = open('rating.txt', 'r')
user_score = 0
for line in rating_file:
    if name == line.split()[0]:
        user_score = int(line.split()[1])

rating_file.close()

options = input()
if options == '':
    available_options = ['rock', 'paper', 'scissors']
else:
    available_options = options.split(',')

computer_options = available_options.copy()


#print(f'available options : {available_options}')

total_options = len(available_options)
half_options = int(total_options / 2)

print('Okay, let\'s start')
user_choice = ''

while user_choice != '!exit':
    user_options = available_options.copy()
    user_choice = input()
    #print(f'avalaible options : {available_options}')
    #print(f'user choice : {user_choice}')

    if user_choice == '!rating':
        print(f'Your rating: {user_score}')

    elif user_choice not in available_options:
        print('Invalid input')

    else:
        user_choice_pos = user_options.index(user_choice)
        random.shuffle(computer_options)
        computer_choice = computer_options[0]
        user_options.remove(user_choice)
        #print(f'computer choice : {computer_choice}')
        #print(f'remaining options : {user_options} ')

        loose_range = user_choice_pos + half_options
        double_options = user_options + user_options
        loose_range = double_options[user_choice_pos:loose_range]
        #print(f'loose range : {loose_range}')

        if user_choice == computer_choice:
            user_score += 50
            print(f'There is a draw ({user_choice})')

        elif computer_choice in loose_range:
            print(f'Sorry, but the computer chose {computer_choice}')

        else:
            user_score += 100
            print(f'Well done. The computer chose {computer_choice} and failed')

print('Bye!')

