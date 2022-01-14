import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        isLogged: sessionStorage.getItem('authToken') !== null,
        username: sessionStorage.getItem('username'),
        firstName: sessionStorage.getItem('firstName'),
        lastName: sessionStorage.getItem('lastName')
    },
    mutations: {
        isLoggedUpdate () {
            this.state.isLogged = sessionStorage.getItem('authToken') !== null
            this.state.username = sessionStorage.getItem('username')
            this.state.firstName = sessionStorage.getItem('firstName')
            this.state.lastName = sessionStorage.getItem('lastName')
        }
    }
})
export default store
