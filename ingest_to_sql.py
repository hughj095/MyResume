import sqlalchemy
from sqlalchemy import create_engine

class Upload_To_SQL:
    def upload():
        # Replace these with your actual database details
        server = 'your_server.database.windows.net'
        database = 'your_database'
        username = 'your_username'
        password = 'your_password'
        driver = 'ODBC Driver 17 for SQL Server'

        # Connection string
        connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

        # Create engine
        engine = create_engine(connection_string)

        # Upload (df.to_sql)
        table_name = 'your_table_name'
        df.to_sql(table_name, engine, if_exists='replace', index=False)