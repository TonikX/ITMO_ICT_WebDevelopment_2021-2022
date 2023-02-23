import Vue from 'vue'
import Vuex from 'vuex'
import forecast from './modules/forecast'
import todayWeather from './modules/todayWeather'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    forecast,
    todayWeather
  }
})
