import sqlalchemy
from sqlalchemy import create_engine
import config

class Upload_To_SQL:
    def upload(df_transactions):
        # Replace these with your actual database details
        server = config.server
        database = 'your_database'
        username = 'your_username'
        password = 'your_password'
        driver = 'ODBC Driver 17 for SQL Server'

        # Connection string
        connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

        # Create engine
        engine = create_engine(connection_string)

        # Upload (df.to_sql)
        table_name = 'executions'
        df_transactions.to_sql(table_name, engine, if_exists='replace', index=False) # could also use if_exists='append'