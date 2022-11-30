import Vue from 'vue'
import VueRouter from 'vue-router'
import HoMe from '../views/HoMe'
import Warriors from '../views/Warriors.vue'
import Warrior from '../views/Warrior'
import WarriorEdit from '../views/WarriorEdit'
import Skills from '../views/Skills'
import Professions from '../views/Professions'

Vue.use(VueRouter)

const routes = [
  { 
    path: '/',
    name: 'home',
    component: HoMe
  },
  { 
    path: '/warriors',
    name: 'Warriors',
    component: Warriors
  },
  { 
    path: '/warrior/:warrior_id',
    name: 'Warrior',
    component: Warrior
  },
  { 
    path: '/warrior/edit/:warrior_id',
    name: 'WarriorEdit',
    component: WarriorEdit
  },
  { 
    path: '/skills',
    name: 'Skills',
    component: Skills
  },
  { 
    path: '/professions',
    name: 'Professions',
    component: Professions
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
