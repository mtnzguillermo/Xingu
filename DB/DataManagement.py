import sqlite3

def InsertExpense(DB_Name, date, field, value, concept, observations):

    ExpenseRoute = "DataBases/"

    ExpenseConnection = sqlite3.connect(ExpenseRoute + DB_Name)
    ExpenseCursor = ExpenseConnection.cursor()

    # TO DO: Calcular code
    ExpenseCursor.execute("INSERT INTO EXPENSES VALUES(code, date, field, value, concept, observations)")

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