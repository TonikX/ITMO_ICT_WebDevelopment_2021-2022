const routes=[
    {path:'/home',component: home},
    {path:'/bill',component: bill}
]
const router=new VueRouter({
    routes
})

const app = new Vue ({
    router
}).$mount('#app')