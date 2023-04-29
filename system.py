import os
import csv
import math

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
# the two lists used for the data collection and fraud algorithm


def salesReport():
    '''Pulls the sales information and stores it in a temporary list'''
    folder = os.getcwd()
    fileName = str(folder) + "\\sales.csv"
    with open(fileName, "r") as readFile:
        salesFile = csv.reader(readFile, delimiter=',')
        # reads the sales file and states the delimiter
        for row in salesFile:
            currentNumber = row[1]
            salesList.append(currentNumber)
            # takes each piece of sales data and appends it to the sales list
    salesList.pop(0)
    # removes the title block from the list
    print("Sales information recorded and prepared for analyzation.")
    
def countRows(rows):
    '''Counts the amount of rows in the sales.csv file'''
    folder = os.getcwd()
    fileName = str(folder) + "\\sales.csv"
    for row in fileName:
        # adds i to "rows" each time the loop executes and returns it's final value
        row[1]
        rows = rows+1
    return rows
            
def benfordLawCheck():
    '''Uses benford's law to check the amount of times each first digit is present in the sales data'''
    benlist = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    # declaring the local list variable and the int variables for each number that could appear
    for i in salesList:
        benford = (i[0])
        benlist.append(benford)
        # appends each first number in each value in the sales list to the "benlist"
    for i in benlist:
        count1 = benlist.count('1')
        count2 = benlist.count('2')
        count3 = benlist.count('3')
        count4 = benlist.count('4')
        count5 = benlist.count('5')
        count6 = benlist.count('6')
        count7 = benlist.count('7')
        count8 = benlist.count('8')
        count9 = benlist.count('9')
        # counts the amount of times each number appears in benlist
    print("Numbers Recorded:", count1, count2, count3, count4, count5, count6, count7, count8, count9)
    total = count1+count2+count3+count4+count5+count6+count7+count8+count9
    detectFraud(count1, total)
    valueList = [count1, count2, count3, count4, count5, count6, count7, count8, count9]
    # States every number recorded and calculates for fraud
    for i in range(9):
        resultsFilePrint_Num(valueList[i], i, total)
    # prints to the results.csv file
        
def detectFraud(num, total):
    '''Checks the percentage of the first digit to see if fraud is present'''
    if numericRep(num, total) == "29%" or numericRep(num, total) == "30%" or numericRep(num, total) == "31%" or numericRep(num, total) == "32%":
        print("Fraud not detected :3")
    else:
        print("!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!")
    # if the calculation is within the allocated percent range, fraud is not detected

def numericRep(num, total):
    '''Calculates the percentage of times a first digit is present in all of the sales data'''
    calculation = num * 100 / total # cross multiply and divide to find the percentage
    calculation  = str(math.trunc(calculation)) + "%" # removes the decimal from the percentage and adds the % sign
    return calculation

def visualRep():
    pass # incomplete as of now, Zoya will complete

def resultsFilePrint_Num(var, num, total):
    '''Prints the numeric representation of the data to the results.csv file'''
    text = "\n" + str(num) + "," + str(numericRep(var, total))
    # given the variable, the number that the variable is assigned to in the list, and the total of each number,
    # the function prints the given number and the percentage to the results.csv file
    folder = os.getcwd()
    fileName = str(folder) + "\\results.csv"
    with open(fileName, "a") as file:
        file.write(text)

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
# the menu that allows for feature selection

# exits once the user types 
print("Program Terminated")