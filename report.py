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
        account_summary = ib.accountSummary()
        portfolio = ib.portfolio()
        total_portfolio_value = 0
        for position in portfolio:
            market_value = position.marketValue()
            total_portfolio_value += market_value
        cash_balance = 0
        for item in account_summary:
            if item.tag == 'CashBalance':
                cash_balance += float(item.value)
        total_portfolio_value += cash_balance
        df_daily = pd.DataFrame(total_portfolio_value)
        Upload_To_SQL.upload(df_transactions, df_daily)
        return total_portfolio_value
        
        

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=3)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
Report.report(ib, date = datetime.date.today())