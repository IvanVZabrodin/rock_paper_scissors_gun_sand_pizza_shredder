#I'm 8 years old
import random
import time
console.alert('How to play' , "To play you need to go into console and type play('choice') and replace choice with one of [rock, paper, scissors, gun, sand, pizza or shredder]" , 'Play')
def timer(t):
	time.sleep(t)
	print("finished")
def play(a):
	r = random.randint(1,7)
	if a == 'rock' and r == 2 or 5:
		print("CPU won:(")
	elif a == 'rock' and r == 1:
 		print("draw:|")
	elif a == 'paper' and r == 3 or 4:
		print("CPU won:(")
	elif a == 'paper' and r == 2:
		print("draw:|")
	elif a == 'scissors' and r == 1 or 4:
		print("CPU won:(")
	elif a == 'scissors' and r == 3:
		print("draw:|")
	elif a == 'gun' and r == 5 or 1:
		print("CPU won:(")
	elif a == 'gun' and r == 4:
		print("draw:|")
	elif a == 'sand' and r == 1 or 2:
		print("CPU won:(")
	elif a == 'sand' and r == 5:
		print("draw:|")
	elif a == 'pizza' and r == 1 or 3:
		print("CPU won:(")
	elif a == 'pizza' and r == 6:
		print("draw:|")
	elif a == 'shredder' and r == 3 or 1:
		print("CPU won:(")
	elif a == 'shredder' and r == 7:
		print("draw:|") 
	else:
	  print("You won!")
	if r == 1:
		print("CPU picked rock")
	elif r == 2:
		print("CPU picked paper")
	elif r == 3:
		print("CPU picked scissors")
	elif r == 4:
		print("CPU picked gun")
	elif r == 5:
		print("CPU picked sand")
	elif r == 6:
		print("CPU picked pizza")
	else:
		print("CPU picked shredder")
	print("THANKS FOR PLAYING🤘🏻!!!")
	print("Do the play() command to play again")
		
