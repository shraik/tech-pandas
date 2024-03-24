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

### Формат вывода

Вариант прямого указания формата колонок. Формат можно установить после вывода данных.
Пример добавления формата цифр, установки формата на колонку №2 и автоподбора ширины колонок по данным.
параметр "18" это ширина колонки в символах, но если использовать автоподбор ширины, то параметр бесполезен.
```
    format1 = writer.book.add_format({"num_format": "#,##0.00;-#,##0.00;-"})
    ws = writer.book.get_worksheet_by_name("Sheet1")
    ws.set_column(2, 2, 18, format1)
    ws.autofit()

```