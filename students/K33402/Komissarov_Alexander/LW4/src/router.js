import Vue from 'vue'
import VueRouter from 'vue-router'

import Registration from "@/views/Registration";
import Login from "@/views/Login";
import About from "@/views/About";
import Author from "@/views/Author";
import Cabinet from "@/views/Cabinet";
import Main from "@/views/Main";


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Main',
        component: Main
    },
    {
        path: '/cabinet',
        name: 'Cabinet',
        component: Cabinet
    },
    {
        path: '/author',
        name: 'Author',
        component: Author
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/registration',
        name: 'Registration',
        component: Registration
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    let isAuthenticated = localStorage.getItem('token');
    if (to.name !== 'Login'&& to.name !== 'Registration' && !isAuthenticated) next({ name: 'Login' })
    else next()
})

export default router