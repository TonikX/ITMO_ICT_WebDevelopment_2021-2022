import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login'
import PersonalPage from '@/views/PersonalPage'
import SignOut from '@/views/SignOut'
import Regitration from '@/views/Regitration'
import Ekipazh from '@/views/Ekipazh'
import Planes from '@/views/Planes'
import Reys from '@/views/Reys'
import Tranzit from '@/views/Tranzit'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signout',
    name: 'SignOut',
    component: SignOut
  },
  {
    path: '/register',
    name: 'register',
    component: Regitration
  },
  {
    path: '/personalpage',
    name: 'PersonalPage',
    component: PersonalPage
  },
  {
    path: '/ekipazh',
    name: 'Ekipazh',
    component: Ekipazh
  },
  {
    path: '/planes',
    name: 'Planes',
    component: Planes
  },
  {
    path: '/reys',
    name: 'reys',
    component: Reys
  },
  {
    path: '/tranzit',
    name: 'tranzit',
    component: Tranzit
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
