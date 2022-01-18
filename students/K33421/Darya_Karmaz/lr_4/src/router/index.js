import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Room from '../components/Room.vue'
import Book from '../components/Book.vue'
import Edit from '../components/Edit.vue'
import Login from '../components/Login.vue'
import SignIn from '../components/SignIn.vue'
import OneBook from '../components/OneBook.vue'
import OneRoom from '../components/OneRoom.vue'
import TakenBook from '../components/TakenBook.vue'

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
    path: '/rooms',
    name: 'Room',
    component: Room
  },
  {
    path: '/books',
    name: 'Book',
    component: Book
  },
  {
    path: '/register',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/edit',
    name: 'Edit',
    component: Edit
  },
  {
    path: '/rooms/:id',
    name: 'OneRoom',
    component: OneRoom
  },
  {
    path: '/books/:id',
    name: 'OneBook',
    component: OneBook
  },
  {
    path: '/books/taken/:id',
    name: 'TakenBook',
    component: TakenBook
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
