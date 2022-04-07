import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from './views/Posts'
import Login from './views/Login'
import Logout from './views/Logout'
import Workers from './views/Workers'
import Assignments from './views/Assignments'
import Applications from './views/Applications'
import ServiceCreate from './views/ServiceCreate'
import OneService from './views/OneService'
import ChangeService from './views/ChangeService'
import Register from './views/Register'
import AssignmentCreate from './views/AssignmentCreate'
import OneAssignment from './views/OneAssignment'
import ChangeAssignment from './views/ChangeAssignment'
import ChangePass from './views/ChangePass'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
        path: '/',
        name: 'posts',
        component: Posts,
        meta: {
            requiresLogin: false
          }
        },
        {
        path: '/login',
        name: 'login',
        component: Login,
        },
        {
        path: '/logout',
        name: 'logout',
        component: Logout,
        },
        {
        path: '/workers',
        name: 'workers',
        component: Workers,
        },
        {
        path: '/assignments',
        name: 'assignments',
        component: Assignments,
        },
        {
        path: '/applications',
        name: 'applications',
        component: Applications,
        },
        {
        path: '/service/create',
        name: 'service_create',
        component: ServiceCreate,
        },
        {
        path: '/one_service',
        name: 'one_service',
        component: OneService,
        },
        {
        path: '/change_service',
        name: 'change_service',
        component: ChangeService,
        },
        {
        path: '/assignment/create',
        name: 'assignment_create',
        component: AssignmentCreate,
        },
        {
        path: '/one_assignment',
        name: 'one_assignment',
        component: OneAssignment,
        },
        {
        path: '/change_assignment',
        name: 'change_assignment',
        component: ChangeAssignment,
        },
        {
        path: '/register',
        name: 'register',
        component: Register,
        },
        {
        path: '/change_password',
        name: 'change_password',
        component: ChangePass,
        },
    ]
})