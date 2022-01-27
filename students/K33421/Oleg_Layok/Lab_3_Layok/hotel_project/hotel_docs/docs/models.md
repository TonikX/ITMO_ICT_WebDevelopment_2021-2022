# Модели
###Room
```    
{
    "number": 210,
    "type": "3",
    "price": 5000,
    "floor": 3,
    "cleaners": [
        1,
        1
    ]
}
```

###Guest
```    
{
    "id": 1,
    "passport_number": "1111474722",
    "name": "Billy",
    "surname": "Armstrong",
    "middlename": "Joe",
    "from_location": "Los Angeles",
    "check_in_date": "2020-12-03",
    "room": 210
}
```

###Staff
```    
{
    "id": 1,
    "name": "Ivan",
    "surname": "Ivanov",
    "middlename": "Ivanovich"
}
```

###Cleaning
```    
{
    "id": 1,
    "date_time": "2022-01-20T12:00:00Z",
    "room": 210,
    "staff": 1
}
```
