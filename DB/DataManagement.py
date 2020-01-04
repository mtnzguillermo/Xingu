import sqlite3
from datetime import datetime

def InsertExpense(DB_Name, date, field, value, concept, observations):

    # Opening connection and creating the cursor
    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()

    # Generation of the new code for the expense
    code = GenerateNewCode(cursor, date)

    ################## Harcode
    virtual = 0.0
    liquid = 0.0
    month_indicator = 0.0
    month_savings = 0.0

    # Sumarizing all input parameters
    expense_values = (code, date, field, value, concept, observations)
    money_values = (code, virtual, liquid, month_indicator, month_savings)

    # Updating DB
    cursor.execute("INSERT INTO EXPENSES VALUES(?, ?, ?, ?, ?, ?)", expense_values)
    cursor.execute("INSERT INTO MONEY VALUES(?, ?, ?, ?, ?)", money_values)

    # Final actions and closing connection
    connection.commit()
    connection.close()

def InsertLoan(DB_Name, date, person, value, concept, observations):

    # Opening connection and creating the cursor
    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()

    # Generation of the new code for the loan
    code = GenerateNewCode(cursor, date)

    ################## Harcode
    virtual = 0.0
    liquid = 0.0
    month_indicator = 0.0
    month_savings = 0.0

    # Sumarizing all input parameters
    loan_values = (code, date, person, value, concept, observations)
    money_values = (code, virtual, liquid, month_indicator, month_savings)

    # Updating DB
    cursor.execute("INSERT INTO EXPENSES VALUES(?, ?, ?, ?, ?, ?)", loan_values)
    cursor.execute("INSERT INTO MONEY VALUES(?, ?, ?, ?, ?)", money_values)

    # Final actions and closing connection
    connection.commit()
    connection.close()

def GenerateNewCode(cursor, date):

    # Turning the date into a entry code
    day_code = int(date.strftime("%Y%m%d")+"000")

    # Setting limits of the day codes
    limits = [day_code, day_code+1000]

    # Checking DB for codes from the same day
    cursor.execute("SELECT CODE FROM MONEY WHERE CODE BETWEEN ? and ?;", limits)
    results = cursor.fetchall()

    # Generating new code
    if len(results) == 0:
        new_code = day_code+1
    else:
        new_code = max(max(results))+1

    return new_code

def GetExpense(code):
    pass

def GetLoan(code):
    pass

def GetDebtPeople(DB_Name):

    #PROVISIONAL   
    import sqlite3
    ExpenseRoute = "DataBases/"

    # Opening connection and creating the cursor
    connection = sqlite3.connect(ExpenseRoute + DB_Name)
    cursor = connection.cursor()

    cursor.execute("SELECT NAME FROM DEBTS")
    results = cursor.fetchall()

    people = []
    for row in results:
        people.append(row[0])

    # Final actions and closing connection
    connection.commit()
    connection.close()

    return(people)