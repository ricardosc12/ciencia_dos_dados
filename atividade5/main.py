import pandas as pd

original_df = pd.read_excel('./OnlineRetail.xlsx')
df = original_df

missing_invoice_no = len(df[pd.isnull(df['InvoiceNo']) == True])

invalid_unit_price = len(df[df['UnitPrice']<0])

