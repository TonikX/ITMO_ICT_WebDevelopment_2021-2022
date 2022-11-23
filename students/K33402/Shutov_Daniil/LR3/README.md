# Бэкенд приложения погоды

## Установка
```shell
pip install -r requrements.txt
python manage.py migrate
python manage.py loaddata cities.json
```

## API
`/api/cities/all/` - список городов

`/api/cities/preferences/` - список городов для пользователя

Остальные части API представлены библиотеками Djoser (`/api/auth`) и drf-yasg (`/swagger`, `/redoc`)