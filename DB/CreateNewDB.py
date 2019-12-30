import sqlite3

def CreateNewDB(DB_Name):

    route = "DataBases/"

    connection = sqlite3.connect(route + DB_Name)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE MONEY (CODE INTEGER, DATE DATE, REAL DOUBLE, VIRTUAL DOUBLE, INDICATOR DOUBLE, SAVINGS DOUBLE))")
    cursor.execute("CREATE TABLE EXPENSES (CODE INTEGER, DATE DATE, FIELD VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")
    cursor.execute("CREATE TABLE LOANS (CODE INTEGER, DATE DATE, PERSON VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")

    connection.close()