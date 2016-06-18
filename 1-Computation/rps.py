# python 2

# Name: JLM
# Date: 06.17.2016
#
#


import random

user = raw_input("Choose your weapon: ")
comp = random.choice( ['rock','paper','scissors'] )

print 'the user (you) chose', user
print 'the comp (I) chose', comp

if user == comp:
    print 'Tie. No fun.'
    
elif user == 'rock':
  if comp == 'paper':
    print 'Paper covers rock. I win. You lose. Sucker.'
  else:
    print 'You smashed my scissors! I lose. Waaaahhh!'
    
elif user == 'paper':
  if comp == 'scissors':
    print 'Imma cut a b*tch. You lose!'
  else:
    print 'Aww. You covered my rock and made me lose.'
    
else:
  if comp == 'paper':
    print 'You cut me! Meanie.'
  else:
    print 'Hulk SMASH! You lose!'
