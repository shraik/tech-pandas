import pandas as pd
import sys

# Считать excel файл
df = pd.read_excel("demodata/SampleData.xlsx", sheet_name="SalesOrders")
# вывести первые 5 строк
print("Заголовок фрейма")
print(df.head(5))

# вывести структуру фрейма
print("\n Структура")
print(df.dtypes)

# настроить "писаря"
writer = pd.ExcelWriter(
    "demodata/out_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS",
    # engine="openpyxl",  # другой вариант движка для записи .xlsx
    engine="xlsxwriter",
)

df.to_excel(writer, sheet_name="Sheet1", startcol=3)
writer.close()

print("\nВывести пути venv. Если пути разные скрипт выполняется в venv")
print(sys.prefix)
print(sys.base_prefix)

print("Okay, exit(0)")
