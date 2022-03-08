# Vuex хранилище

Полностью типизированное Vuex хранилище. Главный модуль доступен по ```$store```

```typescript
export class StoreTypescript {
  $config !: NuxtRuntimeConfig

  auth !: AuthModule
  cities !: CitiesModule
  forecast !: ForecastModule

  constructor($store: Store<any>, $config: NuxtRuntimeConfig) {
    this.$config = $config

    this.auth = getModule(AuthModule, $store)
    this.cities = getModule(CitiesModule, $store)
    this.forecast = getModule(ForecastModule, $store)
  }
}
```

## Всего есть 3 главных модуля:
 - Модуль авторизации
 - Модуль городов и избранного
 - Модуль прогнозов

Код для каждого модуля представлен ниже:

### Модуль авторизации

```typescript
import { Module, Mutation, VuexModule } from 'vuex-module-decorators'

type payload = {
  key: string
  value: any
}

type TUser = {
  id: number
  email: string
  username: string
}

@Module({
  name: 'auth',
  stateFactory: true,
  namespaced: true,
})
export default class AuthModule extends VuexModule {
  user: TUser | null = null
  loggedIn: boolean = false

  @Mutation
  SET(payload: payload) {
    if (payload.key === 'user') {
      this.user = payload.value
    } else if (payload.key === 'loggedIn') {
      this.loggedIn = payload.value
    }
  }
}
```


### Модуль городов и избранного

```typescript
import { Module, Mutation, VuexModule } from 'vuex-module-decorators'
import { TCitiesStoreData } from "~/types/store";
import { VuexAction } from "nuxt-property-decorator";
import { $axios } from "~/utils/axios";
import axios from "axios";
import useRequests from "~/utils/useRequests";

@Module({
  name: 'cities',
  stateFactory: true,
  namespaced: true,
})
export default class CitiesModule extends VuexModule {
  data: TCitiesStoreData[] = []
  favorites: number[] = []
  search: number[] = []
  error: string = ''

  get isCityInFavorites() {
    return (cityID: number) => this.favorites.includes(cityID)
  }

  get searchedCitiesOnly() {
    return this.data.filter(item => this.search.includes(item.id))
  }

  @Mutation
  setError(error: string) {
    this.error = error
  }

  @Mutation
  addData(data: TCitiesStoreData) {
    this.data.push(data)
  }

  @Mutation
  setData(data: TCitiesStoreData[]) {
    this.data = data
  }

  @Mutation
  addCityFavorite(cityID: number) {
    this.favorites.push(cityID)
  }

  @Mutation
  removeCityFavorite(cityID: number) {
    this.favorites = this.favorites.filter(item => item !== cityID)
  }

  @Mutation
  addCitySearch(cityID: number) {
    this.search.push(cityID)
  }

  @VuexAction({ rawError: true })
  async fetchCity(city: string | null) {
    if (city === null) {
      this.setError('Введите город')
      return
    }

    const filtered: TCitiesStoreData[] = this.data.filter(
      item => (item.local_names.ru.toLowerCase() === city.toLowerCase()) 
        || (item.query === city.toLowerCase()))

    if (filtered.length !== 0) {
      this.addCitySearch(filtered[0].id)
      return filtered[0]
    }

    let result: TCitiesStoreData | null = null

    let params = new URLSearchParams()
    params.set('q', city)

    try {
      const response = await $axios.get(`/city`, { params })

      if (response.data.length === 0) {
        this.setError(`Не удалось найти указанный город`)
      } else {
        let data: TCitiesStoreData = response.data[0]
        data.query = city.toLowerCase()

        this.addCitySearch(data.id)
        this.addData(data)
        this.setError('')
        result = data
      }
    } catch (e) {
      if (axios.isAxiosError(e)) this.setError(
        `Не удалось получить данные о городе. Сервер вернул ${e.response?.status}`)
      else {
        this.setError('Неизвестная ошибка!')
        console.error(e)
      }
    }

    return result
  }

  @VuexAction({ rawError: true })
  async favoritesChange(cityID: number) {
    const isAdd = !this.isCityInFavorites(cityID)
    const method = isAdd ? 'post' : 'delete'
    const url = `/city/${cityID}/favorite`

    const result = await useRequests($axios).performRequest(method, url)

    if (result.response) {
      isAdd ? this.addCityFavorite(cityID) : this.removeCityFavorite(cityID)
    } else if (result.fallback) {
      this.setError(`Не удалось ${isAdd ? 'сохранить' : 'удалить'} город. Сервер вернул 
      ${result.fallback.response?.status}`)
    }
  }
}
```


### Модуль прогнозов

```typescript
import { Module, Mutation, VuexModule } from 'vuex-module-decorators'
import { VuexAction } from "nuxt-property-decorator";
import { TCitiesStoreData, TForecastStoreData } from "~/types/store";
import { $axios } from "~/utils/axios";
import useRequests from "~/utils/useRequests";

@Module({
  name: 'forecast',
  stateFactory: true,
  namespaced: true,
})
export default class ForecastModule extends VuexModule {
  data: TForecastStoreData[] = []
  error: string = ''

  @Mutation
  setError(error: string) {
    this.error = error
  }

  @Mutation
  addData(data: TForecastStoreData) {
    this.data.push(data)
  }

  @Mutation
  setData(data: TForecastStoreData[]) {
    this.data = data
  }

  @VuexAction({ rawError: true })
  async fetchForecast(cityData: TCitiesStoreData) {
    let result: TForecastStoreData | null = null

    let filtered: TForecastStoreData[] = this.data.filter(
      forecast => forecast.city.id === cityData.id)
    if (filtered.length !== 0) return filtered[0]

    const respresult = await useRequests($axios).performRequest('get', 
      `/city/${cityData.id}/forecast`)

    if (respresult.response) {
      result = respresult.response.data[0] as TForecastStoreData
      result.city = cityData
      this.setError('')
      this.addData(result)
    } else if (respresult.fallback) {
      this.setError(`Не удалось получить прогноз погоды для города 
      ${cityData.local_names.ru}. Сервер вернул 
      ${respresult.fallback.response?.status}`)
    }

    return result
  }
}
```
