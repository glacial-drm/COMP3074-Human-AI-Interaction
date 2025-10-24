# 4.1.3 Working with a database
    # To view db content    
        # Use SELECT statements within code
        # Use software (e.g. SQLite browser)
import sqlite3

connection = sqlite3.connect('database.db') # Create connection to db

cursor = connection.cursor() # Open cursor from connection

cursor.execute ('''CREATE TABLE Corpus ( documentId text , documentContent text , documentTopic text )''') # Create table in db, ERASES THE CONTENT OF POTENTIALLY ALREADY EXISING TABLE

cursor.execute (" INSERT INTO Corpus VALUES ( ' doc1 ','This is an  example document for the corpus ', 'example ')") # Insert row into table

connection.commit() # Commit changes to db
connection.close() # Close connection