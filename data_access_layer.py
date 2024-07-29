import pyodbc
from typing import List, Dict

class DataAccessLayer:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_customer_data(self) -> List[Dict[str, object]]:
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode FROM Customers")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
