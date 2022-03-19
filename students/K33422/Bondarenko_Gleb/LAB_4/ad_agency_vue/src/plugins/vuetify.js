// src/plugins/vuetify.js

import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#353535',
        secondary: '#f4ebdb',
        anchor: '#8a8a8a'
      }
    }
  }
})

export default vuetify
