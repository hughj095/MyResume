class Sell:
    def sell_stock():
        global x, TICKER, df_transactions, SHARES, strike_price, sell_time, current_time, sell_price, held, df_budget, budget, stop_loss
        print('start of sell function')
        ### ADD TRANSACTION_ID HERE
        df_transactions.iloc[x,5] = sell_price
        df_transactions.iloc[x,6] = sell_time
        df_transactions.iloc[x,7] = sell_price * SHARES
        df_transactions.iloc[x,8] = df_transactions.iloc[x,7] - df_transactions.iloc[x,4]
        df_transactions.iloc[x,9] = current_time
        if sell_price < 0.99 * strike_price:
            df_transactions.iloc[x,10] = 'stop loss'
            stop_loss = True
        print(f'sold {TICKER}') 
        held = False
        df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)
        budget = budget + sell_price * SHARES
        df_budget.iloc[0,0] = budget
        df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)