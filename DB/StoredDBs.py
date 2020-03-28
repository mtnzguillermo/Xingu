
import sqlite3
from os import listdir

def CheckIfExists(DB_Name, storage_path):

    stored_DBs = GetStoredDBs(storage_path)

    if DB_Name in stored_DBs:
        output = True
    else:
        output = False

    return(output)

def GetStoredDBs(storage_path):
    
    file_names = listdir(storage_path)

    return(file_names)

def CheckPassword(password_entry, DB_Name, storage_path):
    
    # Opening connection and creating the cursor
    connection = sqlite3.connect(storage_path+DB_Name)
    cursor = connection.cursor()

    # Reading the correct password
    cursor.execute("SELECT PASSWORD FROM PASSWORD")
    DB_output = cursor.fetchone()
    correct_password = DB_output[0]
    print(correct_password)

    # Final actions and closing connection
    connection.commit()
    connection.close()

    # Output
    if password_entry == correct_password:
        output = True
    else:
        output = False

    return(output)