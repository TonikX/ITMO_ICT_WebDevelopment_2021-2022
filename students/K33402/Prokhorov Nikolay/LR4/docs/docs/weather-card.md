# Карточка погоды в городе

Отображает погоду в городе. Единственным параметром принимает объект Forecast типа TForecastStoreData 

```html
<weather-card :forecast="forecast" />
```


```typescript
export type OnecallResponse = {
  lat:             number
  lon:             number
  timezone:        string
  timezone_offset: number
  current:         Current
  minutely:        Minutely[]
  hourly:          Current[]
  daily:           Daily[]
  alerts:          Alert[]
}

export type TCitiesStoreData = {
  id: number
  country: string
  lat: number
  local_names: { [key: string]: string } & { ru: string }
  lon: number
  name: string
  state: string

  query: string
}

export type TForecastStoreData = OnecallResponse & {
  city: TCitiesStoreData
}
```
