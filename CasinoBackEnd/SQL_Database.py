import sqlite3

class SQL_Databases:
    """This class is used for executing SQL queries using Python. Default path to 'CasinoDatabase.db'"""

    def __init__(self, path="CasinoDatabase.db") -> None:
        """Connect to database and create a cursor."""

        self.__database = path
        self.con = sqlite3.connect(self.__database) 
        self.cur = self.con.cursor()

    def __del__(self):
        """Delete cursor and close database when destructed."""

        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()

    def set_database_path(self, path):
        """Set database path or name."""
        self.__database = path
    
    def create_table(self, tableName, tableAttributes):
        """Create table [tableName] ([tableAttributes]);"""

        command = "Create table " +tableName +" (" +tableAttributes +");"
        self.cur.execute(command)
        
        self.con.commit()
    
    def create_table_input_terminal(self):
        """Open consol input: Create table [consoleInput] ([consoleInput]);"""
        
        tableName = input("Enter name of table: ")

        self.cur.execute(".tables")
        queary_result = self.cur.fetchall()
        tableFound = 0
        for i in queary_result:
            if i==tableName:
                tableFound = 1

        if tableFound==0:
            tableAttributes = input("Enter table attributes and type seperated by commas: ")
            command = "Create table " +tableName +" (" +tableAttributes +");"
            self.cur.execute(command)
            print(tableName +" Table Created")
        else:
            print("Table of that name already exists.")

        self.con.commit()


    def queary_table_all_atributes(self, tableName):
        """Select * From [tableName]"""

        sqlCommand = "Select * From " +tableName
        self.cur.execute(sqlCommand)
        return self.cur.fetchall()
        

    def select_from_where(self, table, row, column, condition):
        """SELECT [ROW] FROM [TABLE] WHERE [COLUMN] = [CONDITION]"""

        self.command = f"SELECT {row} from {table} where {column} = {condition};"
        self.exec_and_commit(self.command)
        result = self.cur.fetchall()
        return result

    def select_from(self, tableName, attributes):
        """Select [attributes] From [tableName]"""
        
        sqlCommand = "Select " +attributes +" From " +tableName
        query_result = self.cur.execute(sqlCommand).fetchall()
        return query_result

    def delete_from_table_where(self, table, column, condition):
        """DELETE FROM [TABLE] WHERE [COLUMN] = [CONDITION]"""

        self.command = f"DELETE from {table} where {column} = {condition};"
        self.exec_and_commit(self.command)


    def insert_into_table_values(self, table, value):
        """INSERT INTO [TABLE] VALUES ([VALUE])"""

        self.command = f"INSERT INTO {table} values ({value});"
        self.exec_and_commit(self.command)

    def exec_and_commit(self, cmd):
        """Execute SQL command and update the database."""
        
        self.cur.execute(cmd)
        self.con.commit()    

    def get_last_rowID(self, table):
        """Get the number of rows ever created."""

        #Note: Even if some rows are deleted, MAX(ROWID) still returns the maximum number ever of rows in the table 
        self.command = f"SELECT MAX(ROWID) from {table};"
        self.cur.execute(self.command)
        self.result = self.cur.fetchall()
        if self.result == None:
            return 0
        return self.result[0][0]

    def get_partial_matches(self, table, row, column, condition):
        """Return an array of rows that contain partial matches of a word in a table."""
        
        self.command = f"SELECT {row} from {table} where {column} like {condition};"
        self.cur.execute(self.command)
        self.result = self.cur.fetchall()
        return self.result
    
    def update_set_where(self, table, newInfo, condition):
        """UPDATE [table] SET [newInfo] WHERE [condition]
        
        Ex:
        UPDATE PlayerMain SET Last = 'Doe', First = 'John' WHERE ID = '12345'
        
        table = "PlayerMain"
        
        newInfo = "Last = 'Doe', First = 'John'"
        
        condition = "ID = '12345'"
        """
        self.command = f"UPDATE {table} SET {newInfo} WHERE {condition}"
        self.exec_and_commit(self.command)

