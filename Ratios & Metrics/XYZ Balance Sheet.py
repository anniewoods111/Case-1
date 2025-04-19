import pandas as pd

balancesheet = 'https://finance.yahoo.com/quote/XYZ/balance-sheet/'
balancesheet_table = pd.read_html(balancesheet)
