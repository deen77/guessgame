import random
print "This is a guess game.\nYou just need to guess a number with given clue.\nLet's play!!"
name=raw_input("\nPlease enter player name: ")
print "Welcome and I wish you good luck %s"%(name)
print "\nYou have only 10 tries. Let's start bro!"
guess_wish = ["Let's guess a number: ", "Give me your number: ", "What's your lucky number?: "]
goodluck_wish = ["Dont give up.", "It's cold.", "It's near.", "Come on you can do it.", "Please try harder!!", "Do you have brain?", "Almost dude."]
lie = ["no", "no", "yes", "no"]
num = random.randrange(1,100)
#print num
tries=0
win=0
tries_remaining=10
while tries < 10:
    guess = input('\n%s' % random.choice(guess_wish))
    lie_status = random.choice(lie)
    if guess == num:
        print('Woww!! Congratulation bro, you made it!! The number is %d' % num)
        win=1
        break
    elif guess > num:
        if lie_status == 'no':
            print('Your number is bigger. %s' % random.choice(goodluck_wish))
        else:
            print('Your number is lower. %s' % random.choice(goodluck_wish))
    elif guess < num:
        if lie_status == 'no':
            print('Your number is lower. %s' % random.choice(goodluck_wish))
        else:
            print('Your number is bigger. %s' % random.choice(goodluck_wish))

    tries += 1

    print("You have %d try left." % (10-tries))

if win == 0:
    print('Game over!!')
    print('The lucky number is %d.'%num) 


    print('You have %d try left.' % (10 - tries))

if win == 0:
    print('Game over!!')

