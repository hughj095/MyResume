import pandas as pd
from ib_insync import *
from datetime import timedelta
import datetime
from ingest_to_sql import Upload_To_SQL

class Report:
    def report(ib, date):
        executions = ib.reqExecutions(ExecutionFilter())
        executions_data = []
        for e in executions:
            executions_data.append({
                'Account': e.execution.acctNumber,
                'Symbol': e.contract.symbol,
                'Side': e.execution.side,
                'Shares': e.execution.shares,
                'Price': e.execution.price,
                'Time': e.execution.time
            })
        df_transactions = pd.DataFrame(executions_data)
        df_transactions['Time'] = pd.to_datetime(df_transactions['Time'])
        account_summary = ib.accountSummary()
        portfolio_items = ib.portfolio()
        total_portfolio_value = 0
        for item in portfolio_items:
            market_value = item.marketValue
            total_portfolio_value += market_value
        cash_balance = 0
        for item in account_summary:
            if item.tag == 'CashBalance':
                cash_balance += float(item.value)
        total_portfolio_value += cash_balance
        df_daily = pd.DataFrame([total_portfolio_value])
        Upload_To_SQL.upload(df_transactions, df_daily, ib)
        return total_portfolio_value
        

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
#Report.report(ib, date = datetime.date.today())