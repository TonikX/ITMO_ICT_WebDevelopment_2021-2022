import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        authToken: '',
        isLogged: false,
        id: '',
        username: '',
        firstName: '',
        lastName: '',
        role: ''
    },
    mutations: {
        isLoggedUpdate (_, params) {
            if (params === undefined) return
            for (const [key, value] of Object.entries(params)) {
                this.state[key] = value
                if (key === 'authToken') {
                    this.state.isLogged = this.state.authToken !== ''
                }
            }
        }
    }
})
export default store
