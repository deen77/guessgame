import random
print "This is a guess game.\nYou just need to guess a number with given clue.\nLet's play!!"
name=raw_input("\nPlease enter player name: ")
print "Welcome and I wish you good luck %s"%(name)
print "You have only ten tries."
guess_wish = ["Let's guess a number: ", "Give me your number: ", "What's your lucky number?: "]
goodluck_wish = ["Dont give up", "It's cold", "It's near", "Come on you can do it", "Please try harder!!", "Do you have brain?", "Almost dude"]
lie = ["yes", "no", "yes", "no", "yes", "no"]
num = random.randrange(1,100)
print num
tries=0
tries_remaining=10
while tries < 10:
    guess = input(random.choice(guess_wish))
    lie_status = random.choice(lie)
    if guess == num:
        print('Woww!! You made it!! The number is %d' % num)
        break
    elif guess > num:
        if lie_status == 'no':
            print('Your number is bigger. Please try again!')
        else:
            print('Your number is lower. Please try again!')
    elif guess < num:
        if lie_status == 'no':
            print('Your number is lower. Please try again!')
        else:
            print('Your number is bigger. Please try again!')

    tries += 1
    print("You have %d try left." % (10-tries))