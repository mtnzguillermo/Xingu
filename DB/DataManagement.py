import sqlite3
from datetime import datetime

def InsertExpense(DB_Name, date, field, value, concept, observations):

    # Opening connection and creating the cursor
    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()

    # Generation of the new code for the expense
    code = GenerateNewCode(cursor, date, field)

    # Updating EXPENSES table in DB
    expense_values = (code, date, field, value, concept, observations)
    cursor.execute("INSERT INTO EXPENSES VALUES(?, ?, ?, ?, ?, ?)", expense_values)
    
    # Updating MONEY table in DB
    UpdateMoney(cursor, code, value)

    # Final actions and closing connection
    connection.commit()
    connection.close()

def InsertLoan(DB_Name, date, person, value, concept, observations):

    # Opening connection and creating the cursor
    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()

    # Updating LOANS table in DB
    loan_values = (date, person, value, concept, observations)
    cursor.execute("INSERT INTO LOANS VALUES(?, ?, ?, ?, ?)", loan_values)

    # Updating DEBTS table in DB
    UpdateDebts(cursor, person, value)

    # Final actions and closing connection
    connection.commit()
    connection.close()

def GenerateNewCode(cursor, date, field):

    # Turning the date into a entry code
    if field == "Mensual":
        day_code = int(date.strftime("%Y%m")+"00000")
    else:
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

    # Opening connection and creating the cursor
    connection = sqlite3.connect(DB_Name)
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

def UpdateMoney(cursor, code, value):

    print("Let's update the MONEY TABLE")
    # Selecting previous monet entry
    cursor.execute("SELECT * FROM MONEY WHERE CODE < ? ORDER BY CODE DESC;", [code])
    previous_entry = cursor.fetchone()

    # Calculating new entry parameters
    total_money = previous_entry[1]+value
    [month_indicator, month_savings] = CalculateMoneyParameters(cursor, code)
    money_values = [code, total_money, month_indicator, month_savings]

    # Inserting entry
    cursor.execute("INSERT INTO MONEY VALUES(?, ?, ?, ?)", money_values)
    print("Entry inserted")

    # Searching for later entries to update
    cursor.execute("SELECT * FROM MONEY WHERE CODE > ? ORDER BY CODE ASC;", [code])
    entries_to_update = cursor.fetchall()

    # Updating all later entries
    for entry in entries_to_update:

        # Searching for the expense asociated with the present MONEY entry
        cursor.execute("SELECT * FROM EXPENSES WHERE CODE = ?;", [entry[0]])
        corresponding_expense = cursor.fetchone()

        # Calculating new parameters
        total_money += corresponding_expense[3]
        [month_indicator, month_savings] = CalculateMoneyParameters(cursor, entry[0])
        money_values = [total_money, month_indicator, month_savings, entry[0]]

        # Updating entry
        cursor.execute("UPDATE MONEY SET VIRTUAL = ?, MONTH_INDICATOR = ?, MONTH_SAVINGS = ? WHERE CODE = ?", money_values)


def UpdateDebts(cursor, person, value):

    cursor.execute("SELECT NAME FROM DEBTS")
    results = cursor.fetchall()

    people = []
    for row in results:
        people.append(row[0])

    if person in people:
        cursor.execute("SELECT VALUE FROM DEBTS WHERE NAME=?;", [person])
        current_value_cursor = cursor.fetchone()
        current_value = current_value_cursor[0]

        value = current_value + value

        debts_values = [value, person]
        cursor.execute("UPDATE DEBTS SET VALUE=? WHERE NAME=?", debts_values)

    else:
        # Sumarizing all input parameters
        debts_values = [person, value]
        # Updating DB
        cursor.execute("INSERT INTO DEBTS VALUES(?, ?)", debts_values)
        
def CalculateMoneyParameters(cursor, code):

    # Reading code
    code_str = str(code)
    year = code_str[0:4]
    month = code_str[4:6]
    day = code_str[6:8]

    # Extracting all monthly incomes/expenses
    limits = [year+month+"00000", year+month+"01000"]
    cursor.execute("SELECT * FROM EXPENSES WHERE CODE BETWEEN ? and ?;", limits)
    monthly_data = cursor.fetchall()

    # Calculating total monthly income
    monthly_income = 0
    for data in monthly_data:
        monthly_income += data[3]

    # Extracting all expenses/incomes during the month until the given day
    limits = [year+month+"01000", str(code)]
    cursor.execute("SELECT * FROM EXPENSES WHERE CODE BETWEEN ? and ?;", limits)
    month_data = cursor.fetchall()

    # Calculating total month expense at the given day
    month_expense = 0
    for data in month_data:
        month_expense -= data[3]
    
    # Calculating days in the given month
    from calendar import monthrange
    month_days = monthrange(int(year), int(month))
    month_length = month_days[1]

    # Calculating month indicator and savings
    projected_expense = monthly_income*float(day)/month_length
    month_indicator = projected_expense-month_expense
    month_savings = monthly_income-month_expense

    return([month_indicator, month_savings])