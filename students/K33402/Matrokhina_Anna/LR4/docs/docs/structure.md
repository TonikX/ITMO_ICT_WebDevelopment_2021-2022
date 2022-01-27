# Структура проекта

## Описание директорий

- assets/
    - Глобальные стили проекта
    - Логотип
- components/
    - Переиспользуемые компоненты
- mixins/
    - Переиспользуемый JS код компонентов
- router/
    - Настройки Vue Router
- store/
    - Vuex Store
- views/
    - Страницы проекта

## Компоненты

На данном этапе в проекте используется лишь один компонент - карточка для отображения информации о погоде Имеет следующие параметры:

```js
{
  id: Number
  weatherid: Number
  title: String
  weather: Number
  pressure: Number
  wind: Number
  windDirection: String
  saveButton: Boolean
  deleteButton: Boolean
  deleteById: Boolean
  noDetailButton: Boolean
}
```

## Миксины

WeatherMixin - миксин для взаимодействия с сервером, получения погорода по названию и прогноза погоды в городе, а так же фильтрация полученных данных по указанной дате

Имеет 3 функции:

```
getWindDirection(windAngle: Number) -> String
async resolveCityName(city: String) -> Result object
async apiCityWeather(city: String, date: String) -> Result object 
```

`Result object` - универсальный тип для функций миксина. Имеет вид `let result = { status: true, data: null, error: null }`
Если `result.status === true`, значит запрос был успешно получен и отфильтрован, необходимые данные доступны в `result.data`
В случае ошибки ее текст сохраняется в `result.error`. В этом случае `result.status` будет равен `false`

# Router

Стандарный конфиг Vue Router. Для добавления новых страниц использовать структуру

```
{
    path: '/',
    name: 'Home',
    component: Home
  },
```

где `path` - URL, `name` - имя страницы для удобвства разработки, `component` - представление страницы

# Store

Vuex хранилище. Хранит информацию о пользователе:

```
state: {
  token: '', 
  username: '',
  email: ''
}
```

Имеет геттер `isLogged`, возвращающий `Boolean` - авторизован пользователь или нет.

# Views

Папка со всеми представлениями системы. Новые представления необходимо добавлять сюда.
