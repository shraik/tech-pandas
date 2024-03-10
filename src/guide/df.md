# Обработка данных в датафрейме

### Варианты удаленния

- Удаление строк c нулевыми значениями в колонке "Col5"
```
df_fakt.dropna(subset="Col5", axis="index", inplace=True)
```

- Удаление колонок "Col1", "Col4"
```
df_fakt.drop(labels=["Col1", "Col4"], axis="columns", inplace=True)
```