import mysql.connector

class CarDatabase:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",  # Replace with your MySQL host
            user="root",        # Replace with your MySQL username
            password="adastra-db",    # Replace with your MySQL password
            database="car_database"  # Replace with your MySQL database name
        )

    def execute_query(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def get_selected_columns(self, columns):
        query = f"SELECT {', '.join(columns)} FROM cars"
        data = self.execute_query(query)
        return data

    def get_filtered_data(self, condition):
        query = f"SELECT * FROM cars WHERE {condition}"
        data = self.execute_query(query)
        return data
