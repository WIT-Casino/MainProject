import sqlite3

class Databases:
    def __init__(self):
        self.database = sqlite.connect("testDB.db")
        self.cursor = database.cursor()
        createDefaultTables()

    def __init__(self, databaseName):
        self.database = sqlite.connect(databaseName)
        self.cursor = database.cursor()
        createDefaultTables()

    def createDefaultTables(self):
        self.cursor.execute(".tables")
        queary_result = self.cursor.fetchall()
        tableFound = 0
        for i in queary_result:
            if i=="Players":
                tableFound = 1

        if tableFound == 0:
            self.cursor.execute("Create table Players (ID INT PRIMARY KEY NOT NULL, LUCK INT NOT NULL, SKILL INT NOT NULL, CHEAT INT NOT NULL);")
            print("Player Table Created")

        tableFound = 0
        for i in queary_result:
            if i=="Games":
                tableFound = 1

        if tableFound == 0:
            self.cursor.execute("Create table Games (gameID INT PRIMARY KEY NOT NULL, gamesPlayed INT NOT NULL, REVENUE INT NOT NULL);")
            print("Games Table Created")

    
    def createTable(self, tableName, tableAttributes):
        self.cursor.execute(".tables")
        queary_result = self.cursor.fetchall()
        tableFound = 0
        for i in queary_result:
            if i==tableName:
                tableFound = 1

        if tableFound==0:
            command = "Create table " +tableName +" (" +tableAttributes +");"
            self.cursor.execute(command)
            print(tableName +" Table Created")
        else:
            print("Table of that name already exists.")

        self.database.commit()
    
    def createTableContained(self):
        tableName = input("Enter name of table: ")

        self.cursor.execute(".tables")
        queary_result = self.cursor.fetchall()
        tableFound = 0
        for i in queary_result:
            if i==tableName:
                tableFound = 1

        if tableFound==0:
            tableAttributes = input("Enter table attributes and type seperated by commas: ")
            command = "Create table " +tableName +" (" +tableAttributes +");"
            self.cursor.execute(command)
            print(tableName +" Table Created")
        else:
            print("Table of that name already exists.")

        self.database.commit()


    def quearyTableAllAtributes(self, tableName):
        sqlCommand = "Select * From " +tableName
        query_result = self.cursor.execute(sqlCommand)
        for i in query_result:
            print(i)

    def quearyTableSpecifiedAttributes(self, tableName, attributes):
        sqlCommand = "Select " +attributes +" From " +tableName
        query_result = self.cursor.execute(sqlCommand)
        for i in query_result:
            print(i)

        









            
