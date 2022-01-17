import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        isLogged: localStorage.getItem('authToken') !== null,
        username: localStorage.getItem('username'),
        firstName: localStorage.getItem('firstName'),
        lastName: localStorage.getItem('lastName'),
        role: localStorage.getItem('role')
    },
    mutations: {
        isLoggedUpdate () {
            this.state.isLogged = localStorage.getItem('authToken') !== null
            this.state.username = localStorage.getItem('username')
            this.state.firstName = localStorage.getItem('firstName')
            this.state.lastName = localStorage.getItem('lastName')
            this.state.role = localStorage.getItem('role')
        }
    }
})
export default store
