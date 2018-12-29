questions = []
answers = []
username = []

def add_question():
	new_question = input("Enter your new question:\n")
	new_answer = input("Please enter your answer:\n")
	new_username = input("please enter your username:\n")
	questions.append(new_question)
	answers.append(new_answer)
	username.append(new_username)
	return print(new_question + " added with " + new_answer + " as the answer.")
	
def show_questions():
	i = 0 
	while i < len(questions):
		print(str(i) + ". " + questions[i])
		i += 1
		
def ask_question():
	Question_number = int(input("enter the number of the question\n"))
	print(questions[Question_number])
	answer = input("enter your answer\n")
	if answer == answers[Question_number]:
		print("CORRECT")
	else:
		print("INCORRECT it was" + answers[Question_number])
		
def show_username():
	User_number = int(input("enter the number of the question\n"))
	print(username[User_number])
	
