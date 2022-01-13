import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        isLogged: sessionStorage.getItem('auth_token') !== null
    },
    mutations: {
        isLoggedUpdate () {
            this.state.isLogged = sessionStorage.getItem('auth_token') !== null
        }
    }
})
export default store
