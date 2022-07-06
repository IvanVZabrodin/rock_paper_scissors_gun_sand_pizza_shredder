import random
choices = ['rock', 'paper', 'scissors', 'shredder', 'pizza', 'gun']

def play(a):
	r = random.randint(0,6)
	c = choices.index(a) 
	print("Computer chose %s" %choices[r])
	if c % 3 == 0 and r % 3 == 2 or c % 3 > r % 3:
		print("Player won")
		return 1
	if c == r:
		print("Draw")
		return 2
	print("Computer won")
	return 0
	
