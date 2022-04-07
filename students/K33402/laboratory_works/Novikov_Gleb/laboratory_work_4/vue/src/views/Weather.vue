<template>
     <div class="container">
          <h2 class="fs-4 mb-5">Ваша погодная сводка, {{ this.$store.getters.USERNAME }}! 😎</h2>
          <div class="row row-cols-1 row-cols-md-3 mt-3 mb-3 text-center">
            <div v-for="data in weatherData" class="col">
              <div class="card mb-4 rounded-3 box-shadow">
                  <img class="card-img" image src="@/assets/city.jpg" width="300" height="150">
                  <div class="card-header py-3">
                    <h4 class="my-0 fw-normal">{{ data.city }}</h4>
                  </div>
                  <div class="card-body">
                    <b-table class="table mt-2 mb-2" striped hover :items="data.weather"></b-table>
                  </div>
              </div>
            </div>
    </div>
     </div>
</template>

<script>
var API_KEY = ''

export default {
  data () {
    return {
      weatherData: [],
      username: this.$store.getters.USERNAME
    }
  },
  async mounted () {
    try {
      const response = await this.axios.get('http://127.0.0.1:8000/town/all/', {headers: {
          'Authorization': `Token ${this.$store.state.token}`
        }})

      console.log('success', response)
      let citiesData = {}
      response.data.towns.forEach(town => {
        citiesData[town.name] = [town.lon, town.lat]
      })
      this.$store.commit('SET_CITIES', citiesData)

    } catch (e) {
      console.log(e)
      console.log(e.response)

      if (e.response) {
        this.errors = e.response.data
      }
    }

    var cities = this.$store.getters.CITIES
    console.log('cities', cities)

    Object.keys(cities).forEach(key => {
      this.axios
        .get('https://api.openweathermap.org/data/2.5/onecall?lat=' + cities[key][0] + '&lon=' + cities[key][1] + '&exclude={daily}' + '&appid=' + API_KEY + '&lang=eng&units=metric')
        .then(response => response.data)
        .then(data => this.weatherData.push({
          city: key,
          weather: [
            { date: 'Сегодня', temp: data.daily[0].temp.day + 'C', prec: data.daily[0].weather[0].description },
            { date: 'Завтра', temp: data.daily[1].temp.day + 'C', prec: data.daily[1].weather[0].description }
          ]
        }))
    })
  }
}
</script>

<style scoped>
.fs-4 {
    text-align: left;
}
</style>
