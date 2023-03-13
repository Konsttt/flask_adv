### Flask. Homework netology: advertisements.

### Что реализовано:
База данных postgres разворачивается в docker-e.
Две связанные таблицы. Adv и Users: таблица с объявлениями и с пользователями.
Пароли хранятся в БД в виде хеша md5.
Пароли проходят валидацию на длину.
Для пользователя реализованы - post, delete
Для объявлений - все методы.
При удалении пользователя, его объявления удаляются каскадом.

### Запуск:

```shell
docker compose up
```
Далее:
<br>server.py - RUN.
<br> client.py - выбираем нужный запрос, остальное комментируем - RUN.