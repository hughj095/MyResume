import pandas as pd
from ib_insync import *

class Report:
    def report(ib):
        df_report = pd.readcsv('')
        # open new tab/sheet
        # pull executions for day
        executions = ib.reqExecutions(ExecutionFilter())
        # put execution items in a df
        # adjust IB time to my time
        # summarize by ticker with columns Bought and Sold
        # Net for day by ticker
        # Total for day
        # Diff vs previous day
        # YTD Net
