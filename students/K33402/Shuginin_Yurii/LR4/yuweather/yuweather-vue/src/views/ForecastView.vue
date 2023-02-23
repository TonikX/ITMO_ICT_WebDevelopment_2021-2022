<template>
  <div class="forecast">
    <Header />
    <main>
        <div class="container pt-4">
            <div class="row mx-auto">
                <div v-if="auth()" class="col-12 d-flex flex-sm-row flex-column justify-content-between align-items-center">
                    <h2 class="text-primary mb-3 mb-sm-0">{{ getHeader }}</h2>
                    <button v-if="not_added(getCityName)" class="btn btn-primary btn-lg" type="button" @click="addFavourite(getCityName)">Add to Favourites</button>
                    <button v-else class="btn btn-success btn-lg" type="button" disabled>Favourite</button>
                </div>
                <div v-else class="col-12 d-flex flex-sm-row flex-column justify-content-between align-items-center">
                    <h2 class="text-primary mb-3 mb-sm-0">{{ getHeader }}</h2>
                    <button class="btn btn-secondary btn-lg" type="button" disabled>Add to Favourites</button>
                </div>
            </div>
            <div class="row mt-4 mx-auto justify-content-center">
                <ForecastCard
                    v-for="Forecast in allForecasts"
                    :key="Forecast.identifier"
                    :Forecast="Forecast"
                />
            </div>
        </div>
    </main>
    <Footer />
    <LogoutModal />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import ForecastCard from '@/components/ForecastCard.vue'
import LogoutModal from '@/components/LogoutModal.vue'
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'ForecastView',
  components: {
    Header,
    Footer,
    ForecastCard,
    LogoutModal
  },

  data: () => ({
    favourites: [],
    Cities: [],
    CitiesNames: []
  }),

  computed: mapGetters(['allForecasts', 'getHeader', 'getCityName']),

  methods: {
    ...mapActions(['getForecasts']),

    not_added (city = '') {
      if (city) {
        return !this.favourites.includes(city)
      }
    },

    data_entered () {
      const url = new URLSearchParams(window.location.search)
      const data = Object
      data.city = url.get('city')
      data.lat = url.get('lat')
      data.lon = url.get('lon')
      return data
    },

    auth () {
      return localStorage.getItem('token')
    },

    async getFavourites () {
      if (localStorage.getItem('token')) {
        const favourites = await fetch('http://localhost:8000/users/', { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        const favouritesJSON = await favourites.json()
        this.favourites = favouritesJSON.Users[0].favourite_cities
      }
    },

    parseCities (toFVRTS = false, city = '') {
      axios
        .get('http://localhost:8000/cities/')
        .then(response => {
          this.Cities = response.data.Cities
          this.CitiesNames = []
          for (let i = 0; i < this.Cities.length; i++) {
            this.CitiesNames.push(this.Cities[i].name)
          }

          if (toFVRTS) {
            this.axios
              .post('http://127.0.0.1:8000/favourites/create', { Favourite: { user_id: Number(localStorage.getItem('user_id')), city_id: this.cityID(city) } }, { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
              .then(this.getFavourites())
              .catch(err => {
                console.error(err)
                window.location.href = 'error?back=1'
              })
          }
        })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    },

    addCity (city) {
      this.axios
        .post('http://127.0.0.1:8000/cities/create', { city: { name: `${city}` } })
        .then(this.parseCities(true, city))
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    },

    addFavourite (city) {
      if (!this.CitiesNames.includes(city)) {
        this.addCity(city)
      } else {
        this.axios
          .post('http://127.0.0.1:8000/favourites/create', { Favourite: { user_id: Number(localStorage.getItem('user_id')), city_id: this.cityID(city) } }, { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
          .catch(err => {
            console.error(err)
            window.location.href = 'error?back=1'
          })
        this.getFavourites()
      }
    },

    cityID (city) {
      for (let i = 0; i < this.Cities.length; i++) {
        if (this.Cities[i].name === city) {
          return this.Cities[i].id
        }
      }
    }
  },

  created () {
    this.getFavourites()
    const cityData = this.data_entered()
    this.getForecasts(cityData)
    this.parseCities()
  }
}
</script>
