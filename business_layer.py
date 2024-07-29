from data_access_layer import DataAccessLayer
from typing import List, Dict

class BusinessLayer:
    def __init__(self, connection_string: str):
        self.dal = DataAccessLayer(connection_string)

    def get_customer_data(self) -> List[Dict[str, object]]:
        return self.dal.get_customer_data()
