# Создание файла excel

Пример вывода датафрейма в файл excel
```
# настроить объект "писарь"
writer = pd.ExcelWriter(
    "demodata/out_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS",
    # engine="openpyxl",  # другой вариант движка для записи .xlsx
    engine="xlsxwriter",
)

df.to_excel(writer, sheet_name="Sheet1", startcol=3)
writer.close()
```

Закрывать объект writer обязательно, иначе данные не будут записаны на диск.