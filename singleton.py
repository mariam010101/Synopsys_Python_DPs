class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to database"
        return cls._instance

    def get_connection(self):
        return self.connection


db1 = DatabaseConnection()
print(db1.get_connection())

db2 = DatabaseConnection()
print(db2.get_connection())

print(db1 is db2)  
