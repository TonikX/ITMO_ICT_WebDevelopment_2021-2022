import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import ChickensList from '../views/Chickens.vue'
import BreedsList from '../views/Breeds copy.vue'
import CagesList from '../views/Cages.vue'
import TasksList from '../views/Tasks.vue'
import WorkersList from '../views/Workers.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/chickenslist',
    name: 'ChickensList',
    component: ChickensList
  },
  {
    path: '/workerslist',
    name: 'WorkersList',
    component: WorkersList
  },
  {
    path: '/taskslist',
    name: 'TasksList',
    component: TasksList
  },
  {
    path: '/breedslist',
    name: 'BreedsList',
    component: BreedsList
  },
  {
    path: '/cageslist',
    name: 'CagesList',
    component: CagesList
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
