import Vue from 'vue'
import Vuex from 'vuex'
import {WeatherModule} from "@/store/weather"
import {CityModule} from "@/store/city"
import axios from "axios";
import router from "@/router";

Vue.use(Vuex)

export const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    timeout: 1000,
    headers: {'Content-type': 'application/json; charset=UTF-8',}
});

const store = new Vuex.Store({
    state: () => ({
        username: '',
        citiesAll: require("@/assets/city.list.min.json"),
        units: localStorage.getItem('units') || 'metric',
        unitsData: {
            standard: {deg: 'K', speed: 'm/s'},
            metric: {deg: '°C', speed: 'm/s'},
            imperial: {deg: '°F', speed: 'm/h'}
        },
        activeCity: {},
        gettingLocation: localStorage.getItem('location'),
        location: JSON.parse(localStorage.getItem('location')) || {},
        daysWeek: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        fullDaysWeek: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    }),
    getters: {},
    mutations: {
        GET_USER(state, data) {
            state.username = data
        },
        ADD_GETTING_LOCATION(state, data) {
            state.gettingLocation = data
        },
        ADD_LOCATION(state, data) {
            state.location = data
            if (data.name) {
                localStorage.setItem('location', JSON.stringify(data))
            } else {
                localStorage.removeItem('location')
            }
        },
        ADD_UNITS(state, data) {
            state.units = data
            localStorage.setItem('units', data)
        },
        REMOVE_CITY(state, id) {
            state.cities = state.cities.filter(city => city?.id !== id)
        },
        RETURN_ALL_CITY(state) {
            state.cities = require("@/assets/city.list.min.json")
        },
        ADD_ACTIVE_CITY(state, data) {
            state.activeCity = data
        }
    },
    actions: {
        REGISTER({dispatch}, payload) {
            instance.post(`/auth/users/`, JSON.stringify(payload))
                .then(function (data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(dispatch('LOGIN', payload))
        },
        LOGIN(store, payload) {
            instance.post(`/auth/jwt/create/`, JSON.stringify(payload))
                .then(function (data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(token => {
                    localStorage.setItem('token', JSON.stringify(token));
                    router.push('/')
                })
        },
        GET_USER({commit, dispatch}) {
            instance
                .get(`/auth/users/me/`, {
                    headers: {
                        Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                    }
                })
                .then(function (data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(user => {
                    commit('GET_USER', user.username)
                    commit('ADD_CITY_MODULE', user.cities || [])
                    commit('REMOVE_ALL_WEATHER_MODULE')
                    dispatch('ADD_WEATHER', user.cities || [])

                })
        },
        ADD_LOCATION(state) {
            if (!("geolocation" in navigator)) {
                return
            }
            navigator.geolocation.getCurrentPosition(res => {
                state.commit('ADD_LOCATION', res)
                state.dispatch('ADD_LOCAL_WEATHER')
                state.commit('ADD_GETTING_LOCATION', true)
            }, () => {
                state.commit('ADD_LOCATION', {})
                state.commit('ADD_GETTING_LOCATION', false)
            })
        },
        ADD_ACTIVE_CITY(state, payload) {
            const data = state.rootState.city.data.find((city) => city === payload)
            if (data === undefined) {
                state.commit('ADD_ACTIVE_CITY', state.state.citiesAll.filter(x => x?.id.toString() === payload)[0], {root: true})
            } else {
                state.commit('ADD_ACTIVE_CITY', data, {root: true})
            }
        }
    },
    modules: {
        weather: WeatherModule,
        city: CityModule,
    }
})

export default store;

