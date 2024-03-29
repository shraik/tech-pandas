# Установка

Описанные ниже инструкции предназначены для windows 10. Для linux пользователей тоже применимы с небольшими зависящими от базового дистрибутива правками.
Для упрощения дальнейшей работы с проектом рекомендую выделить отдельный каталог.
Например C:\pypa

Подразумевается, что интерпретатор Python уже установлен и добавлен в системные переменные PATH.
Использование системы виртуальных окружений Python позволит выполнить установку всех файлов в один каталог.

Создание виртуального окружения
> c:\>pypa\python -m venv .\.venv

Для использования виртуального окружения в терминале, его необходимо активировать.
Скрипты активации добавляются при установке и расположены в: 
> C:\dist3\.venv\Scripts

# Установка необходимых библиотек с использованием "pip"

Для удобства в каталоге "C:\pypa" создать файл 1.cmd следующего содержания:
```
chcp 65001
call .venv\Scripts\activate.bat 
```

1. Запустить cmd в каталоге "C:\pypa"
1. Для активации venv запустить созданный скрипт 1.cmd или команду .venv\Scripts\activate.bat
    после активации venv изменяется вид приглашения командной строки с 
    "C:\pypa>" -> "(.venv) C:\pypa>"
1. Запустить команду установки библиотек:
> (.venv) C:\pypa>\pip install pandas, xlsxwriter, openpyxl

# Дополнительная информация
Для вывода информации о venv в котором выполняется ваш скрипт можно воспользоваться следующим кодом:
```
import sys
print(sys.prefix)
print(sys.base_prefix)
```

# Среда разработки
К сожалению, когда ваш скрипт достигнет первой сотни строк или даже раньше, вам не обойтись без среды разработки с возможностью отладки (пошагового выполнения).
Я использую для разработки - "Visual Studio Code" + Python 3.12.
Если ваши исходные данные можно загружать в интернет, можно воспользоваться  Github Codespaces.

Описания настройки среды разработки в этой документации не будет.