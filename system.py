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

def salesReport():
    pass

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
    else:
        print("Please type in a valid option (1,2, or 0): ")

# exits once the user types 
print("Program Terminated")