import sqlite3

def CreateNewDB(DB_Name, Password, initial_money):

    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE MONEY (CODE INTEGER, VIRTUAL DOUBLE, MONTH_INDICATOR DOUBLE, MONTH_SAVINGS DOUBLE)")
    cursor.execute("CREATE TABLE EXPENSES (CODE INTEGER, DATE DATE, FIELD VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")
    cursor.execute("CREATE TABLE LOANS (DATE DATE, PERSON VARCHAR(20), VALUE DOUBLE, CONCEPT VARCHAR(50), OBSERVATIONS VARCHAR(200))")
    cursor.execute("CREATE TABLE DEBTS (NAME VARCHAR(20), VALUE DOUBLE)")
    cursor.execute("CREATE TABLE PASSWORD (PASSWORD VARCHAR(20))")

    cursor.execute("INSERT INTO MONEY VALUES(?, ?, ?, ?)", [0, initial_money, 0.0, 0.0])
    cursor.execute("INSERT INTO PASSWORD VALUES(?)", [Password])

    connection.commit()
    connection.close()

#CreateNewDB("DataBases/Prueba", 1000.0)