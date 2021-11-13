"""
Goals not yet completed:
6) platform

"""

#import modules
from sklearn import tree
import tkinter as tk

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

#function called upon button click
def getUserInput():
    #error handler
    try:
        #collecting user input
        num1 = entry1.get()
        num2 = entry2.get()
        num3 = entry3.get()
        num4 = entry4.get()

        #turning user input into format for the AI to handle
        testlist = [[num1, num2, num3, num4]]

        #calculations
        resultplace = clf.predict(testlist)
         
    except ValueError:
        resultplace = "Careful not to input words!"

    results2["text"] = resultplace

#Displays the GUI
window = tk.Tk()
window.title("AI game")
instructions = tk.Label(text = "Hello! This is a game between you and a simple AI.")
instructions2 = tk.Label(text = "Here's how it works: ")
instructions3 = tk.Label(text = "You will give the AI a series of 4 numbers consisting of the numbers 0 and 1, like \"0101\" \n" +
                        "The rule, which only you and I know, is that the furthestmost value would be the correct one, in this case \"1\"\n"
                         + "Enter a value in each text box, and then click \"Guess?\" when done, and the AI will guess below. \n" + 
                        "Disclaimer: Do not enter words, and avoid using numbers other than 0 and 1 because there may be unintended results!")

entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
entry4 = tk.Entry()

calculate = tk.Button(
                    text = "Guess?",
                    width = 15,
                    height = 3,
                    bg = "gray",
                    fg = "blue",
                    command = getUserInput
                    
    )
    
results = tk.Label(text = "Results: ")
results2 = tk.Label(text = "", fg = "green")

#Makes the widgets visible
instructions.pack()
instructions2.pack()
instructions3.pack()
entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
calculate.pack()
results.pack()
results2.pack()

#handles user interactions
window.mainloop()
