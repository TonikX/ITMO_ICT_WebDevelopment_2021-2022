import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import SignInPage from "@/views/auth/SignInPage";
import SignUpPage from "@/views/auth/SignUpPage";
import ToursPage from "@/views/ToursPage";
Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/tours/:id',
        name: 'ToursPage',
        component: ToursPage
    },
    {
        path: '/signin',
        name: 'SignIn',
        component: SignInPage
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUpPage
    },
]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    let isAuthenticated = localStorage.getItem('token');
    if (to.name !== 'SignIn'&& to.name !== 'SignUp' && !isAuthenticated) next({ name: 'SignIn' })
    else next()
})
export default router