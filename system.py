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
salesList = []
benfordList = []

def salesReport():
    '''Pulls the sales information and stores it in a temporary dictionary file'''
    folder = os.getcwd()
    fileName = str(folder) + "\\sales.csv"
    with open(fileName, "r") as readFile:
        salesFile = csv.reader(readFile, delimiter=',')
        # reads the sales file and states the delimiter
        for row in salesFile:
            currentNumber = row[1]
            salesList.append(currentNumber)
    salesList.pop(0)
    print("Sales information recorded and prepared for analyzation.")
    
def countRows(rows):
    folder = os.getcwd()
    fileName = str(folder) + "\\sales.csv"
    for row in fileName:
        row[1]
        rows = rows+1
    return rows
            
def benfordLawCheck():
    pass

def numericRep(num):
    calculation = ("Frequency of", num, ":", benfordList[num] * 100 / countRows(0))
    return calculation

def visualRep():
    pass

def resultsFilePrint():
    folder = os.getcwd()
    fileName = str(folder) + "\\results.csv"
    with open(fileName, "w") as file:
        for i in range(9):
            file.write(str(numericRep(i)))

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
