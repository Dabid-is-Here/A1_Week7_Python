# let's explore some functions and how to write them
# and also what they do

# my version is found in the master branch in the file named "RPSGame.py"

def greeting():
    # say hello
    print("Hello from your first function!")


# this is how you call or invoke a function
greeting()


def greetings(msg="Hello there", num=0):
    print("Our function says", msg, "The second arg is", num)


greetings()
greetings("This is an argument.", 1)
greetings("Why are we arguing?", 2)

myVariableNumber = 0


def someMath(num1=2, num2=5):
    global myVariableNumber

    myVariableNumber = num1 + num2
    return num1 + num2


sum = someMath()
print("Our sum variable is:", sum, "myVariableNumber is also", sum)
