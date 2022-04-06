<template>
  <div class="favourites">
    <Header />
    <main>
        <div class="container py-4">
            <div class="row">
                <div class="col-12">
                    <h3 class="d-flex align-items-center justify-content-center text-primary">
                        <img src="@/images/star.png" width="35" height="35" class="d-inline-block align-text-top me-3">
                        Favourites
                        <img src="@/images/star.png" width="35" height="35" class="d-inline-block align-text-top ms-3">
                    </h3>
                </div>
            </div>
            <div class="row mt-4 mx-auto">
                <FavouritesCard
                    v-for="Forecast in todayWeather"
                    :key="Forecast.id"
                    :Forecast="Forecast"
                    @click="del(Forecast.city)"
                />
            </div>
            <div class="row">
                <div class="col-12 d-flex justify-content-center">
                    <a class="btn btn-primary btn-lg" href="/" role="button">Add new location</a>
                </div>
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
import FavouritesCard from '@/components/FavouritesCard.vue'
import LogoutModal from '@/components/LogoutModal.vue'
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'FavouritesView',
  components: {
    Header,
    Footer,
    FavouritesCard,
    LogoutModal
  },

  data: () => ({
    favourites: [],
    Cities: []
  }),

  computed: mapGetters(['todayWeather']),

  methods: {
    ...mapActions(['getTodayWeather']),

    del (city) {
      axios
        .delete(`http://localhost:8000/favourites/delete?user_id=${Number(localStorage.getItem('user_id'))}&city_id=${this.cityID(city)}`, { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        .then(response => {
          console.log(response.data)
          this.getFavourites()
        })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    },

    async getFavourites () {
      if (localStorage.getItem('token')) {
        const favourites = await fetch('http://localhost:8000/users/', { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        const favouritesJSON = await favourites.json()
        this.favourites = favouritesJSON.Users[0].favourite_cities
        this.getTodayWeather(favouritesJSON.Users[0].favourite_cities)
      }
    },

    parseCities () {
      axios
        .get('http://localhost:8000/cities/')
        .then(response => {
          this.Cities = response.data.Cities
        })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
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
    this.parseCities()
    this.getFavourites()
  },

  beforeCreate () {
    if (!localStorage.getItem('token')) {
      this.$router.push('/login')
    }
  }
}
</script>
