import pandas as pd
import sys

df = pd.read_excel("demodata/SampleData.xlsx", sheet_name="SalesOrders")
print(df.head())

writer = pd.ExcelWriter(
    "demodata/out_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS",
    engine="openpyxl",
)

df.to_excel(writer, sheet_name="Sheet1", startcol=3)

writer.close()
print("Okay, exit(0)")

print(sys.prefix)
print(sys.base_prefix)