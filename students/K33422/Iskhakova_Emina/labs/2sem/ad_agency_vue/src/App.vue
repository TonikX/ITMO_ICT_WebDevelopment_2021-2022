<template>
 <v-app>
   <v-app-bar
     app
     color="primary"
     dark
   >
     <v-app-bar-nav-icon @click="drawer = true"> </v-app-bar-nav-icon>
     <div class="d-flex align-center">
       <h1 class="headline">Рекламное агентство</h1>
     </div>

     <v-spacer></v-spacer>

     <v-btn v-if='auth' icon @click='AccountDetails'>
       <v-icon>mdi-account</v-icon>
     </v-btn>
     <div class="mx-2"></div>

     <v-btn icon @click='goHome'>
       <v-icon>mdi-home</v-icon>
     </v-btn>
     <div class="mx-2"></div>

     <v-btn icon>
       <v-icon v-if='!auth' @click='login' >mdi-login-variant</v-icon>
       <v-icon v-if='auth' @click='logout' >mdi-logout-variant</v-icon>
     </v-btn>

   </v-app-bar>
   <v-navigation-drawer
     absolute temporary
     dark
     v-if="auth"
     v-model="drawer"
   >
     <v-list
       nav
       dense
     >
       <v-list-item
         v-for="item in items"
         :key="item.title"
         @click=item.link
       >
         <v-list-item-icon>
           <v-icon>{{ item.icon }}</v-icon>
         </v-list-item-icon>
         <v-list-item-content>
           <v-list-item-title>{{ item.title }}</v-list-item-title>
         </v-list-item-content>
       </v-list-item>
     </v-list>
   </v-navigation-drawer>
   <v-main class="d-flex align-center text-center">
     <router-view />
   </v-main>
 </v-app>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'App',
  created () {
    if (localStorage.getItem('token')) {
      $.ajaxSetup({
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      })
    }
  },
  components: {
    // NavDrawer
  },
  computed: {
    auth () {
      if (localStorage.getItem('token')) {
        return true
      } else {
        return false
      }
    }
  },

  methods: {
    login () {
      this.$router.push({ name: 'signin' })
    },
    logout () {
      localStorage.removeItem('token')
      window.location = '/'
    },
    goHome () {
      this.$router.push({ name: 'about' })
    },
    AccountDetails () {
      this.$router.push({ name: 'accountdetails' })
    },
    client () {
      this.$router.push({ name: 'client' })
    },
    servicePL () {
      this.$router.push({ name: 'servicepl' })
    },
    materialsPL () {
      this.$router.push({ name: 'materialspl' })
    },
    executor () {
      this.$router.push({ name: 'executor' })
    },
    request () {
      this.$router.push({ name: 'request' })
    },
    chosenServices () {
      this.$router.push({ name: 'chosenservices' })
    },
    chosenMaterials () {
      this.$router.push({ name: 'chosenmaterials' })
    },
    workGroup () {
      this.$router.push({ name: 'workgroup' })
    },
    invoice () {
      this.$router.push({ name: 'invoice' })
    },
    paymentOrder () {
      this.$router.push({ name: 'paymentorder' })
    }
  },
  data () {
    return {
      items: [
        { title: 'Клиенты', icon: 'mdi-account', link: this.client },
        { title: 'Прайс-лист на услуги', icon: 'mdi-format-list-bulleted', link: this.servicePL },
        { title: 'Прайс-лист на материалы', icon: 'mdi-format-list-bulleted', link: this.materialsPL },
        { title: 'Исполнители', icon: 'mdi-account-tie', link: this.executor },
        { title: 'Заявки', icon: 'mdi-account-question', link: this.request },
        { title: 'Выбранные услуги', icon: 'mdi-cart-arrow-down', link: this.chosenServices },
        { title: 'Выбранные материалы', icon: 'mdi-cart-arrow-down', link: this.chosenMaterials },
        { title: 'Рабочие группы', icon: 'mdi-account-group', link: this.workGroup },
        { title: 'Счета на оплату', icon: 'mdi-cash', link: this.invoice },
        { title: 'Платежные поручения', icon: 'mdi-cash-check', link: this.paymentOrder }
      ],
      drawer: false
    }
  }
}
</script>
