import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import Registration from "../views/Registration.vue"
import Profile from "../views/Profile.vue"
import Experts from "../views/Experts.vue"
import Participants from "../views/Participants.vue"
import Report from "../views/Report.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Report',
    component: Report
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
    path: '/register',
    name: 'Register',
    component: Registration
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/experts/',
    name: 'Experts',
    component: Experts
  },
  {
    path: '/participants',
    name: 'Participants',
    component: Participants
  },
  {
    path: '/report',
    name: 'Report',
    component: Report
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
