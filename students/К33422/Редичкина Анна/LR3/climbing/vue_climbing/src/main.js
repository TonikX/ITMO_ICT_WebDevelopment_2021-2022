import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import 'vue-material-design-icons/styles.css'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

new Vue({
  router,
  vuetify,
  axios,
  render: function (h) { return h(App) }
}).$mount('#app')
