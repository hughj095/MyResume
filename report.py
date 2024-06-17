import pandas as pd
from ib_insync import *
from datetime import datetime, timedelta

class Report:
    def report(ib, date):
        executions = ib.reqExecutions(ExecutionFilter())
        df_transactions = pd.DataFrame(executions)
        # adjust IB time to my time (less 6 hours)
        datetime.strptime(df_transactions['time'], '%Y-%m-%d %H:%M:%S')
        df_transactions['time'] = df_transactions['time'] - timedelta(hours=6)
        # summarize by ticker with columns Bought and Sold, reset index
        df_transactions = df_transactions.groupby('Ticker').resetindex()
        # Net for day by ticker
        df_transactions['Net'] = df_transactions['SLD'] - df_transactions['BOT']
        # Total for day
        total = sum(df_transactions['Net'])
        # Diff vs previous day
        # YTD Net
        # put into Excel
        excel_path = r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.xlsx'
        writer = pd.ExcelWriter(excel_path, engine='openpyxl', mode='a')

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=3)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
Report.report(ib, date = datetime.date.today())