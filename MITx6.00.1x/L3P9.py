'''
The program works as follows: you (the user)
thinks of an integer between 0 (inclusive) and
100 (not inclusive). The computer makes guesses,
and you give it input - is its guess too high or
too low? Using bisection search, the computer will
guess the user's secret number!
'''

print "Please think of a number between 0 and 100!"

hi = 100
lo = 0
stop = False
comp_guess = (hi + lo) / 2
while not stop:
    print "Is your secret number " + str(comp_guess) + "?"
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to "
                         "indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_inp == 'c':
        stop = True
    elif user_inp == 'h':
        hi = comp_guess
    elif user_inp == 'l':
        lo = comp_guess
    else:
        print "Sorry, I did not understand your input."

print 'Game over. Your secret number was: ' + str(comp_guess)
