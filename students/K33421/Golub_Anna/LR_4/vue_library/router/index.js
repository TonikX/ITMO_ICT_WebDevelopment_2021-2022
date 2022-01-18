import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home'
import BookList from '@/views/BookList'
import Book from '@/views/Book'
import SignUp from '@/views/SignUp'
import SignIn from '@/views/SignIn'
import ReaderProfile from '@/views/ReaderProfile'
import ReaderProfileEdit from '@/views/ReaderProfileEdit'
import BookTakeOut from '@/views/BookTakeOut'
import BookReturn from '@/views/BookReturn'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/library/home',
      name: 'home',
      component: Home
    },
    {
      path: '/library/books',
      name: 'catalogue',
      component: BookList
    },
    {
      path: '/library/books/:id',
      name: 'book',
      component: Book
    },
    {
      path: '/library/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/library/signin',
      name: 'signin',
      component: SignIn
    },
    {
      path: '/library/profile',
      name: 'reader_profile',
      component: ReaderProfile
    },
    {
      path: '/library/profile/edit',
      name: 'reader_profile_edit',
      component: ReaderProfileEdit
    },
    {
      path: '/library/take_out/',
      name: 'take_out',
      component: BookTakeOut
    },
    {
      path: '/library/return/:id',
      name: 'return',
      component: BookReturn
    }
  ]
})
