import pandas as pd

df= pd.read_excel("demodata/SampleData.xlsx",sheet_name='SalesOrders')  
print(df)

writer= pd.ExcelWriter("path_to_file.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay",)

df.to_excel(writer, sheet_name="Sheet1", startcol=3)