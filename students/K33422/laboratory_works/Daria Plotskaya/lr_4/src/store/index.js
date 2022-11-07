import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from "@/router";

Vue.use(Vuex)

const instance = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
    headers: {'Content-Type': 'application/json',}
});


const store = new Vuex.Store({
    state: {
        id: null,
        username: '',
        toursList: [],
        tourElement: {},
        totalPrice: null,
        showComments: true
    },
    getters: {
        toursList(state) {
            return state.toursList
        },
        tourElement(state) {
            return state.tourElement
        },
        totalPrice(state) {
            return state.totalPrice
        },
        username(state) {
            return state.username
        },
        showComments(state) {
            return state.showComments
        },
        id(state) {
            return state.id
        },
    },
    mutations: {
        setUser(state, payload) {
            state.id = payload.id
            state.username = payload.username
        },
        setTours(state, payload) {
            state.toursList = payload
        },
        setTourElement(state, payload) {
            state.tourElement = payload
        },
        setTotalPrice(state, payload) {
            state.totalPrice = payload
        },
        setShowComments(state, payload) {
            state.showComments = payload
        },
    },
    actions: {
        Register(store, payload) {
            instance.post(`/auth/users/`, JSON.stringify(payload))
                .then(function (data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(function () {
                    store.dispatch('Login', {
                        username: payload.username,
                        password: payload.password,
                    })
                })
        },
        Login(store, payload) {
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
        mountedProfile({commit}) {
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
                    commit('setUser', {id: user.id ,username: user.username})
                })
        },
        toursList({commit}) {
            instance.get(`/tours/`, {
                headers: {
                    Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                }
            }).then(function (data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(tours => {
                    commit('setTours', tours)
                })
        },
        toursElement({commit}, payload) {
            instance.get(`/tours/${payload}`, {
                headers: {
                    Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                }
            }).then(function (data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(tourElement => {
                    commit('setTourElement', tourElement)
                })
        },
        reservations({commit},payload) {
            instance.post(`/reservations/`, JSON.stringify(payload),{
                headers: {
                    Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                }
            }).then(function (data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(data => {
                    commit('setTotalPrice', data.total_price)
                })
        },
    }
})
export default store;
