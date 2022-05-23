
from random import randrange
import math
#import sys

def main():
    gamer = input('Please input yout name: ')
    #open('output.txt','a').write(f'Please input yout name: {gamer} ')
    game_mode = input(f'Hello {gamer}! please choose game mode\n guess the numder, press 1 \n Computer to guess the number, press 2: \n ')
    #open('output.txt','a').write(f'Hello {gamer}! please choose game mode\n guess the numder, press 1 \n Computer to guess the number, press 2: \n ')
    lower_bound = input('please enter lover bound: ')
    #open('output.txt','a').write('please enter lover bound: ')
    upper_bound = input('please enter higher bound: ')
   # open('output.txt','a').write('please enter higher bound: ')
    while game_mode.isdigit() == False or lower_bound.isdigit() ==False  or upper_bound.isdigit()  == False:
        print('Enter only nimber!')
        game_mode = input(f'Hello {gamer}! please choose game mode\n guess the numder, press 1 \n Computer to guess the number, press 2: \n ')
        lower_bound = input('please enter lover bound: ')
        upper_bound = input('please enter higher bound: ')
    game_mode = int(game_mode)
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
   
   
   
    if lower_bound > upper_bound:
        lower_bound,upper_bound = upper_bound, lower_bound
        
    if game_mode == 1:
        guess_the_number_user(lower_bound, upper_bound)
    elif game_mode == 2:
        guess_the_number_computer(lower_bound, upper_bound)
        
def guess_the_number_user(lower_bound,upper_bound):
    number_to_guess = randrange(lower_bound, upper_bound)
    user_guess = math.inf #ცვლადის ინციალიზაცია უსასრულობით(ვირჩევთ ისეთ რიცხვს რომელიც არ შეიძლება რომ იყოს სწორი პასუხი ანუ უსასრულოვას)
    guess_counter = 0 # ითვლის ცდებს
    
    while number_to_guess != user_guess:
        guess_counter = guess_counter +1
        user_guess = int(input(f'guess the number between {lower_bound} and {upper_bound} : ')) # f ფორმატირება 
       # open('output.txt','a').write(f'guess the number between {lower_bound} and {upper_bound} : ')
        if user_guess < number_to_guess:
            print("to small, try again")
           # open('output.txt','a').write('to small, try again')
        elif user_guess > number_to_guess:
            print('to big, try again')
        print(f'cogretulations! you guessed the number: {number_to_guess} in {guess_counter} tries')
           ## open('output.txt','a').write(f'cogretulations! you guessed the number: {number_to_guess} in {guess_counter} tries')
           
    game_over = input('To return to menu press the(m) button. to quit the game press ENTER: ')
   # open('output.txt','a').write('To return to menu press the(m) button. to quit the game press ENTER: ')
    if game_over == 'm':
        print('______________________________________________________________________________\n')
      #  open('output.txt','a').write('____________________________________________________________')
        main()
    return 0
    
def guess_the_number_computer(lower_bound, upper_bound):
    feedback = ' '# ინიციალიზაცია
    computer_guess = math.inf
    guess_counter_computer = 0
    while feedback != 'c':
        guess_counter_computer += 1 
        computer_guess = randrange(lower_bound, upper_bound)
        feedback = input(f'Is {computer_guess} correct(c), too low(l) or too high(h): ')
        if feedback == 'l':
            lower_bound = computer_guess + 1
        elif feedback == 'h':
            upper_bound = computer_guess -1
        if lower_bound == upper_bound:
            guess_counter_computer +=1
            print(f'only number left is {lower_bound}')
            computer_guess == lower_bound
            break
        
    print(f'Computer guessed the number {computer_guess} in {guess_counter_computer} tries ')              
    game_over = input('To return to menu press the(m) button. to quit the game press ENTER: ')
    if game_over == 'm':
        print('______________________________________________________________________________\n')
       
        main()
    return 0 
       
main()
