import sqlite3

def CreateNewDB(DB_Name):

    route = "DataBases/"

    connection = sqlite3.connect(route + DB_Name)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE EXPENSES (DATE DATE, FIELD VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")
    cursor.execute("CREATE TABLE LOANS (DATE DATE, PERSON VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")

    connection.close()