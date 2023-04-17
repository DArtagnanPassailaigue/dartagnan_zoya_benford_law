import os
import csv

def printMenu():
    '''The menu that allows users to choose an action in the program'''
    print('''
          Sales System\n
          1. Report on total sales\n
          2. Check for fraud in sales data\n
          0. Quit\n
          Enter menu option (1,2,or 0): 
          ''')
    
userInput = ""
reportOption = "1"
fraudOption = "2"
exitCondition = "0"
salesDict = []
word = "Sales"

def salesReport():
    '''Pulls the sales information and stores it in a temporary dictionary file'''
    folder = os.getcwd()
    fileName = str(folder) + "\\sales.csv"
    with open(fileName, "r") as readFile:
        salesFile = csv.reader(readFile, delimiter=',')
        # reads the sales file and states the delimiter
        for row in salesFile:
            currentNumber = row[1]
            salesDict.append(currentNumber)
    salesDict.pop(0)
    print(salesDict)

def benfordLawCheck():
    pass

def numericRep():
    pass

def visualRep():
    pass

def resultsFilePrint():
    pass

while userInput != exitCondition:
    printMenu() 
    userInput = input() 
    if userInput == reportOption:
        salesReport()
    elif userInput == fraudOption: 
        benfordLawCheck()
    elif userInput == exitCondition:
        pass
    else:
        print("Please type in a valid option (1,2, or 0): ")

# exits once the user types 
print("Program Terminated")