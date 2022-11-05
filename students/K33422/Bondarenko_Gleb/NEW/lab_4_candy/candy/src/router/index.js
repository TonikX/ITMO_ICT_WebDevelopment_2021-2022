import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView'
import AboutView from '../views/AboutView'
import Main from '../views/MainView'
import SignIn from '../views/SignIn'
import SignUp from '../views/SignUp'
import ReqView from '../views/ReqView'
import ReqCreate from '../views/ReqCreate'
import CandiesView from '../views/CandiesView'
import CandiesCreate from '../views/CandiesCreate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/candies/',
    name: 'CandiesView',
    component: CandiesView
  },
  {
    path: '/candies/create/',
    name: 'CandiesCreate',
    component: CandiesCreate
  },
  {
    path: '/req/',
    name: 'ReqView',
    component: ReqView
  },
  {
    path: '/req/create/',
    name: 'ReqCreate',
    component: ReqCreate
  },
  {
    path: '/sign-in/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up/',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/main/',
    name: 'Main',
    component: Main
  },
  {
    path: '/aboutview',
    name: 'AboutView',
    component: AboutView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
