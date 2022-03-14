import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    username: 'Default',
    password: null,
    token: null,
    cities: { Moscow: [55.751244, 37.618423], 'Saint Petersburg': [59.57, 30.19], Perm: [58.0, 56.3167] },
    chosenCities: ['Moscow', 'Saint Petersburg', 'Perm'],
    weather: [],
    lastWeatherUpdate: Date.now() // Date
  },
  getters: {
    USERNAME (state) {
      return state.username
    },
    PASSWORD (state) {
      return state.password
    },
    TOKEN (state) {
      return state.token
    },
    CITIES (state) {
      return state.cities
    },
    CHOSEN_CITIES (state) {
      return state.chosenCities
    },
    WEATHER (state) {
      return state.weather
    },
    LAST_WEATHER_UPDATE (state) {
      return state.lastWeatherUpdate
    }
  },
  mutations: {
    SET_CITIES (state, payload) {
      state.cities = payload
    },
    SET_WEATHER (state, payload) {
      state.weather = payload
    },
    REMOVE_CHOSEN_CITY (state, payload) {
      state.chosenCities.remove(payload)
    },
    ADD_CHOSEN_CITY (state, payload) {
      state.chosenCities.add(payload)
    },
    SET_WEATHER_UPDATE (state, payload) {
      state.weather = payload
    },
    SET_USERNAME (state, payload) {
      state.username = payload
    },
    SET_PASSWORD (state, payload) {
      state.password = payload
    },
    SET_TOKEN (state, payload) {
      state.token = payload
    }
  },
  actions: {
    SET_WEATHER (context, payload) {
      context.commit('SET_WEATHER', payload)
    },
    SET_WEATHER_UPDATE (context, payload) {
      context.commit('SET_WEATHER_UPDATE', payload)
    },
    SET_USERNAME (context, payload) {
      context.commit('SET_USERNAME', payload)
    },
    SET_TOKEN (context, payload) {
      context.commit('SET_TOKEN', payload)
    },
    SET_PASSWORD (context, payload) {
      context.commit('SET_PASSWORD', payload)
    }
  }
})
