def play(g):
	AG = input("Question:" + str(g) + ". Now guess the answer.")
	a = input("answer")
	if AG == a:
		print("CORRECT")
	else:
		print("wrong it is " + str(a))
