import sqlalchemy
from sqlalchemy import create_engine
import pyodbc
import config

class Upload_To_SQL:
    def upload(df_transactions, df_daily):
        # Replace these with your actual database details
        server = config.server
        database = config.database
        username = config.username
        password = config.password
        driver = 'ODBC Driver 17 for SQL Server'

        # Connection string
        connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

        # Create engine
        engine = create_engine(connection_string, connect_args={"connect_timeout": 60})

        # Upload (df.to_sql)
        #table_name = 'executions' # could be dbo.executions
        #df_transactions.to_sql(table_name, engine, if_exists='replace', index=False) # could also use if_exists='append'

        table_name = 'portfolio_total' # could be dbo.executions
        df_daily.to_sql(table_name, engine, if_exists='replace', index=False) # could also use if_exists='append'