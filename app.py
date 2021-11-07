# This is a comment. This program adds two numbers.

# This function does the math
def addTwoNumbers(num1, num2):
	answer = num1 + num2
	showMeTheOutput(answer)

def showMeTheOutput(theSomething):
	print(theSomething)

# This calls the functions
def main():
	addTwoNumbers(3, 5)

# This is the main entry point
if __name__ == "__main__":
    main()
