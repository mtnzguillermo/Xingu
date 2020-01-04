import sqlite3

def InsertExpense(DB_Name, date, field, value, concept, observations):

    ExpenseRoute = "DataBases/"

    ExpenseConnection = sqlite3.connect(ExpenseRoute + DB_Name)
    ExpenseCursor = ExpenseConnection.cursor()

    # TO DO: Calcular code
    code = 20200103001

    values = (code, date, field, value, concept, observations)

    ExpenseCursor.execute("INSERT INTO EXPENSES VALUES(?, ?, ?, ?, ?, ?)", values)

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