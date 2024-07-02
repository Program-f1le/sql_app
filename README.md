Чтобы запустить нужны: pydantic, fastapi, sqlalchemy, uvicorn. Капируем рипозиторий к себе на пк. Дальше в терменале пишем uvicron sql_app.main:app --reload. 
В терменале появится строка: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit). Открываем в браузере http://127.0.0.1:8000/docs, появляется swagger документация.
(Не забудте проверить соединение с бд!)

