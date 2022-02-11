"""
Script to play a text-based version of Quasar from Mass Effect

The rules are explained in the specifications below.  For the optimal strategy to
maximize your winnings, see

    https://masseffect.fandom.com/wiki/Quasar

Author: Connor Braaten
Date: January 21, 2022
"""
import random
from urllib import response
import introcs


# Do not touch these first two functions. They are finished for you.
def prompt(prompt,valid):
    """
    Returns the choice from a given prompt.

    This function asks the user a question, and waits for a response.  It checks
    if the response is valid against a list of acceptable answers.  If it is not
    valid, it asks the question again. Otherwise, it returns the player's answer.

    Parameter prompt: The question prompt to display to the player
    Precondition: prompt is a string

    Parameter valid: The valid reponses
    Precondition: valid is a tuple of strings
    """
    # Ask the question for the first time.
    response = input(prompt)

    # Continue to ask while the response is not valid.
    while not (response in valid):
        print('Invalid option. Choose one of '+str(valid))
        print()
        response = input(prompt)

    return response


def payout(bet,score):
    """
    Returns the winnings for a game of quasar.

    Winnings are payout-bet.  So winning your bet (on a score of 17) has a net of 0.

    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0

    Parameter score: the quasar score
    Precondition: score is an int >= 0
    """
    if score == 20:
        return bet
    elif score == 19:
        return round(0.5*bet)
    elif score == 18:
        return round(0.25*bet)
    elif score == 17:
        return 0
    elif score == 16:
        return round(-0.5*bet)
    elif score == 15:
        return round(-0.75*bet)

    # Everything else is a total loss
    return -bet


# Complete these functions
def get_bet(credits):
    """
    Returns the number of credits bet by the user.

    This function asks the user to make a bet

        Make a bet:

    If bet is not an integer, it responds with the error message

        The bet must be an integer.

    If bet is 0 or less, it responds with the error message

        The bet must be a positive integer.

    Finally, if bet is more than credits, it responds with the error message

        You do not have enough credits for that bet.

    It continues to ask for a bet until the user gives a valid answer.

    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    starter = False
    bet = 0

    while not starter:
        try:
            bet_num = input('Make a bet: ')
            new_bet = int(bet_num)

            if new_bet <= 0:
                print('The bet must be a positive integer.')

            elif new_bet > credits:
                print('You do not have enough credits for that bet.')

            else:
                bet = bet + new_bet
                return bet
                
        
        except:
                print('The bet must be an integer.')


def session(bet):
    """
    Returns the payout after playing a single session of quasar.

    The game starts by randomly choosing a number 1-8 and then displaying

        Your score is X.

    (where X is the number chosen). It then prompts the user with the following options:

        Choose (a) 4-7, (b) 1-8, or (s)top:

    If the user chooses 'a' or 'b', it picks a random number, adds it to the score,
    and then displays the score again.  If the user chooses 's' OR the new score is
    20 or more, the session is over.

    Once the session ends, if the user goes over 20, the function prints out

        You busted.

    However, if the user hits 20 exactly, the function prints out

        Quasar!

    Nothing extra is printed if the user is below 20.

    It then prints out

        You won X credits.

    or
        You lost X credits.

    as appropriate, where X is the payout (if X is 0, this is considered a win). When
    the session is done, the function returns the payout.

    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0
    """
    score = 0
    score = score + random.randint(1,8)
    
    print('Your score is '+str(score)+'.')

    starter = True

    while starter:
        user = prompt('Choose (a) 4-7, (b) 1-8, or (s)top: ',('a','b','s'))
        if user == 'a':
            roll_a = random.randint(4,7)
            score = score + roll_a
            print('Your score is '+str(score)+'.')
            if score > 20:
                print('You busted.')
                starter = False
            elif score == 20:
                print('Quasar!')
                starter = False
            else:
                starter

        elif user == 'b':
            roll_b = random.randint(1,8)
            score = score + roll_b
            print('Your score is '+str(score)+'.')
            if score > 20:
                print('You busted.')
                starter = False
            elif score == 20:
                print('Quasar!')
                starter = False
            else:
                starter

        else:
            user == 's'
            score = score
            starter = False

    if score <= 15:
        accepted_bet = payout(bet,score)
        print('You lost '+str(abs(accepted_bet))+' credits.')

    elif 16 >= score <= 19:
        accepted_bet = payout(bet,score)
        print('You lost '+str(abs(accepted_bet))+' credits.')

    elif score > 20:
        accepted_bet = payout(bet,score)
        print('You lost '+str(abs(accepted_bet))+' credits.')

    else:
        score == 20
        accepted_bet = payout(bet,score)
        print('You won '+str(accepted_bet)+' credits')

    return accepted_bet


def play(credits):
    """
    Plays Quasar until the player quits or is broke.

    The game starts by announcing

        You have X credits.

    where X is the number of credits.  It gets a bet from the user and plays a session
    of Quasar.  When done, it adds the payout to the score and repeats the message above.

    If the user reaches 0 credits, the game is over.  Otherwise, it asks

        Do you want to (c)ontinue or (p)ayout?

    If the user chooses 'c', the process repeats (get a bet, play a session, etc.)

    When done, the game prints

        You leave with X credits.

    assuming X > 0. However, if X is 0 it instead prints

        You went broke.

    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    print('You have '+str(credits)+' credits.')

    user_session = session(get_bet(credits))
    credits = credits + user_session

    print('You have '+str(credits)+' credits.')

    starter = True

    while starter:
        if credits == 0:
            starter = False
            return print('You went broke.')

        user = prompt('Do you want to (c)ontinue or (p)ayout? ',('c','p'))
        
        if user == 'c': 
            user_session2 = session(get_bet(credits))
            credits =  credits + user_session2
            print('You have '+str(credits)+' credits.')

        else:
            return print('You leave with '+str(credits)+' credits.')




# Script Code
# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
    play(1000)