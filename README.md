# приложение FastAPI - Crud

# подключение к postgres через докер-компос

docker compose up -d pg
docker compose stop pg
docker compose down
docker compose start pg
sudo systemctl stop postgresql

# для работы с бд использую dbeaver-ce

Новое соединение выбираем postgres

```
Host - localhost
Port - 5432
Database - tasks
Username - user
Password - password
```


poetry add alembic
cd crud_app
alembic init -t async alembic 

для форматирования кода
poetry add --group dev black
