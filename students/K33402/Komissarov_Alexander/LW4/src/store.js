import Vue from 'vue'
import Vuex from 'vuex'
import router from "@/router";

Vue.use(Vuex)

const APIKEY = '9e73e45fff9d9ceee3eabbec55b3bee8'
const URL = `http://api.openweathermap.org/data/2.5/onecall?appid=${APIKEY}&exclude=current,hourly,minutely&units=metric&lang=ru`
const HOST = 'http://127.0.0.1:8000/api'

const store = new Vuex.Store({
        state: {
            weatherApiData: [],
            userCity: [],
            cities: [],
        },
        getters: {
            weatherApiData(state) {
                return state.weatherApiData
            },
            userCity(state) {
                return state.userCity
            },
            cities(state) {
                return state.cities
            },
        },
        mutations: {
            setWeatherApiData(state, payload) {
                state.weatherApiData = payload
            },
            setCities(state, payload) {
                state.cities = payload
            },
            setUserCity(state, payload) {
                state.userCity = payload
            },
        },
        actions: {
            getWeatherApiData({commit}, payload) {
                fetch(`${URL}&lat=${payload.lat}&lon=${payload.lon}`, {method: 'GET'})
                    .then(response => response.json())
                    .then(data => {
                            commit('setWeatherApiData', data.daily)
                        }
                    )
            },
            Registration({dispatch}, payload) {
                fetch(`${HOST}/auth/users/`, {
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        method: 'POST',
                        body: JSON.stringify(payload)
                    }
                )
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .then(() => {
                        dispatch('Login', {
                            username: payload.username,
                            password: payload.password,
                        })
                    })
            },
            Login(store, payload) {
                fetch(`${HOST}/auth/jwt/create/`, {
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        method: 'POST',
                        body: JSON.stringify(payload)
                    }
                )
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .then(data => {
                        localStorage.setItem('token', JSON.stringify(data))
                        router.push('/')
                    })
            },
            getCities({commit}) {
                fetch(`${HOST}/cities/`, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    method: 'GET',
                })
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .then(data => {
                        commit('setCities', data)
                    })
            },
            getUserCities({commit}) {
                fetch(`${HOST}/choices/`, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                    },
                    method: 'GET',
                })
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .then(data => {
                        commit('setUserCity', data)
                    })
            },
            addUserCity({dispatch}, payload) {
                fetch(`${HOST}/choices/`, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                    },
                    method: 'Post',
                    body: JSON.stringify(payload)
                })
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .then(() => {
                        dispatch('getUserCities')
                    })
            },
            delUserCity({dispatch}, payload) {
                fetch(`${HOST}/choices/${payload}/`, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                    },
                    method: 'Delete',
                })
                    .then(response => {
                            if (response.ok) {
                                return response.json();
                            }
                            return Promise.reject(`Ошибка ${response.status}`);
                        }
                    )
                    .finally(() => {
                        dispatch('getUserCities')
                    })
            }
        },
    }
)

export default store