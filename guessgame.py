import random
print "This is a guess game.\nYou just need to guess a number with given clue.\nLet's play!!"
name=raw_input("\nPlease enter player name: ")
print "Welcome and I wish you good luck %s"%(name)
print "You have only ten tries."
guess_wish=["Let's guess a number", "Give me your number", "What's your lucky number?"]
goodluck_wish=["Dont give up", "It's cold", "It's near", "You've gone too far mate!!", "Please try harder next time", "Do you have brain", "Almost near dude"]
lie=["yes", "no"]
num=random.randrange(1,100)
print num
tries=0
tries_remaining=10
while tries < 10:
    guess=random.choice(guess_wish)
    if tries < 5:
        if guess == num:
            print random.choice(lie)
        else:
            print random.choice(lie)
    elif tries == 5:
        if guess == num:
            print "You awesome %s .. i know u can do it"%(name)
        else:
            print "Please work harder %s"%(name)
            print "The answer is %d"%(num)
    else:
        (tries == 5)
        print "%s...your brain is not working mate!!!"%(name)
        print "The answer is %d"%(num)
    tries += 1