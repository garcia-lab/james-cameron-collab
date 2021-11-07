# This is a comment. This program adds a couple of numbers.

# This function does the math
def sumOfTwoNumbers(num1, num2):
	answer = num1 + num2
	showMeTheOutput(answer)

def showMeTheOutput(theSomething):
	print(theSomething)

# This calls the functions
def main():
	sumOfTwoNumbers(4, 6)

# This is the main entry point
if __name__ == "__main__":
    main()
