#import modules
from sklearn import tree

"""

The situation we are going to simulate is
determining whether or not the AI can
guess the right number (which is the last value in the list)

"""

#defines the training data
training_input = [[0,0,0,1], [0,0,0,0],[0,1,1,0],[0,1,0,1],[1,0,1,0],[1,0,0,1],[1,1,1,0],[1,1,1,1]]
#defines the training outputs
training_output = [1, 0, 0, 1, 0, 1, 0, 1]

#building the classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_input, training_output)

def displayTextInstructions():
    #For text only interface
    print("Hello! This is a game between you and a simple AI.")
    print("Here's how it works: ")
    print("   You will give the AI a series of 4 numbers consisting of the numbers 0 and 1, like \"0101\"")
    print("   The AI is trying to guess which column is special.")
    print("   The rule, which only you and I know, is that the last value would be the correct one, in this case \"1\"")
    print("   Disclaimer: Do not enter words, and avoid using numbers other than 0 and 1 because there may be unintended results!")
    print()

def getUserInput():
    
    try:
        num1 = int(input("Enter the first number:   "))
        num2 = int(input("Enter the second number:   "))
        num3 = int(input("Enter the third number:   "))
        num4 = int(input("Enter the fourth and final number:   "))

        testlist = [[num1, num2, num3, num4]]

        print("Guessing \"", num1, num2, num3, num4, "\" ...")
        print(clf.predict(testlist))
        
    except ValueError:
        print("Careful not to input words!")

def main():
    keep_going = True
    response_received = False
    
    displayTextInstructions()
    
    while keep_going:
        keep_going = True
        response_received = False
        getUserInput()

        print()
        response = input("Would you like to play again? Acceptable answers include y, yes, n, or no   ")
        while response_received == False:
            if response.lower() == "no" or response.lower() == "n":
                keep_going = False
                response_received = True
            elif response.lower() == "yes" or response.lower() == "y":
                keep_going = True
                response_received = True
            else:
                response = input("Acceptable answers include yes, y, n, and no. Try again?" + "\t")

main() 
