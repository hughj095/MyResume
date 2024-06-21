import pandas as pd
from ib_insync import *
from datetime import timedelta
import datetime
from ingest_to_sql import Upload_To_SQL

class Report:
    def report(ib, date):
        executions = ib.reqExecutions(ExecutionFilter())
        df_transactions = pd.DataFrame(executions)
        df_transactions['time'] = df_transactions['time'] - timedelta(hours=4)
        Upload_To_SQL.upload(df_transactions)
        
        

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=3)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
Report.report(ib, date = datetime.date.today())