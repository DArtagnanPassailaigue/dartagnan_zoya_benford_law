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
    for i in salesList:
        benford = (i[0])
        benlist.append(benford)
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
    print("Numbers Recorded:", count1, count2, count3, count4, count5, count6, count7, count8, count9)
    total = count1+count2+count3+count4+count5+count6+count7+count9
    detectFraud(count1, total)
    valueList = [count1, count2, count3, count4, count5, count6, count7, count8, count9]
    for i in range(9):
        resultsFilePrint_Num(valueList[i], i, total)
        
def detectFraud(num, total):
    if numericRep(num, total) == "29%" or numericRep(num, total) == "30%" or numericRep(num, total) == "31%" or numericRep(num, total) == "32%":
        print("Fraud not detected :3")
    else:
        print("!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!FRAUD DETECTED!!")

def numericRep(num, total):
    calculation = num * 100 / total
    calculation  = str(calculation) + "%"
    return calculation

def visualRep():
    pass

def resultsFilePrint_Num(var, num, total):
    text = "\n" + str(num) + "," + str(numericRep(var, total))
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

# exits once the user types 
print("Program Terminated")
