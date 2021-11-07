# This is a comment. This program adds two numbers.

# This function does the math
def addIt(num1, num2):
	answer = num1 + num2
	showMeTheOutput(answer)

# This just prints to the console
def showMeTheOutput(theSomething):
	print(theSomething)

# This calls the functions
def main():
	addIt(4, 6)

# This is the main entry point
if __name__ == "__main__":
    main()
