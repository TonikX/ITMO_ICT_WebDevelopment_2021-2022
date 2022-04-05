import Vue from 'vue'
import EventBus from './EventBus'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
Vue.prototype.$bus = EventBus

new Vue({
  router,
  vuetify,
  axios,
  render: h => h(App)
}).$mount('#app')
