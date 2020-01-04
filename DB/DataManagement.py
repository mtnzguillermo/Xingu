import sqlite3

def InsertExpense(DB_Name, date, field, value, concept, observations):

    ExpenseRoute = "DataBases/"

    ExpenseConnection = sqlite3.connect(ExpenseRoute + DB_Name)
    ExpenseCursor = ExpenseConnection.cursor()

    # TO DO: Calcular code
    code = 20200103001
    virtual = 0.0
    liquid = 0.0
    month_indicator = 0.0
    month_savings = 0.0

    expense_values = (code, date, field, value, concept, observations)
    money_values = (code, date, virtual, liquid, month_indicator, month_savings)

    ExpenseCursor.execute("INSERT INTO EXPENSES VALUES(?, ?, ?, ?, ?, ?)", expense_values)
    ExpenseCursor.execute("INSERT INTO MONEY VALUES(?, ?, ?, ?)", money_values)

    ExpenseConnection.commit()

    ExpenseConnection.close()

def InsertLoan(DB_Name, date, person, value, concept, observations):

    LoanRoute = "DataBases/"

    LoanConnection = sqlite3.connect(LoanRoute + DB_Name)
    LoanCursor = LoanConnection.cursor()

    # TO DO: Calcular code
    LoanCursor.execute("INSERT INTO LOANS VALUES(code, date, person, value, concept, observations)")

    LoanConnection.commit()

    LoanConnection.close()

def GetCodes(month, year):
    pass

def GetExpenses(codes):
    pass

def GetLoans(codes):
    pass