#Загрузка xlsx файла в pandas

пример кода загрузки файла

```
import pandas as pd

df = pd.read_excel("demodata/SampleData.xlsx", sheet_name="SalesOrders")
print(df.head())
```