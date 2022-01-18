# Bookings app
Built using FastAPI and Tortoise ORM

# Local deploy
```
docker-compose up --build
```

# Migrations
```
docker exec bookings_fastapi aerich migrate
docker exec bookings_fastapi aerich upgrade
```
