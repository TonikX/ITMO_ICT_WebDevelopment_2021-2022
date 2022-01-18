import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Landing from '../views/Landing.vue'
import Logout from '../views/Logout.vue'
import Signin from '../views/Signin.vue'
import Airplanes from '../views/Airplanes.vue'
import Flight from '../views/Flight.vue'
import Transits from '../views/Transits.vue'
import Admin from '../views/Admin.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout
    },
    {
        path: '/signup',
        name: 'Signup',
        component: Signin
    },
    {
        path: '/',
        name: 'Landing',
        component: Landing
    },
    {
        path: '/airplanes',
        name: 'Airplanes',
        component: Airplanes
    },
    {
        path: '/schedule',
        name: 'Schedule',
        component: Flight
    },
    {
        path: '/transits',
        name: 'transits',
        component: Transits
    },
    {
        path: '/administration',
        name: 'administration',
        component: Admin
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
