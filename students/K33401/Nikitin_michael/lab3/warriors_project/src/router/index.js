import Vue from 'vue'
import VueRouter from 'vue-router'
import Warriors from '../views/Warriors.vue'

Vue.use(VueRouter)

const routes = [
  { 
    path: '/warriors',
    name: 'warriors',
    component: Warriors
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
