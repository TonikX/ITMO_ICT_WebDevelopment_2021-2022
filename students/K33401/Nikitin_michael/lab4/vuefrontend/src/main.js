import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import store from './store'
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';



Vue.config.productionTip = false
Vue.prototype.$http = axios

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })

    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
