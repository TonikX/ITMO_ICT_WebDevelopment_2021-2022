<template>
  <nav>
    <v-toolbar class="blue">
      <v-toolbar-title>
        <span class="white--text">Airport</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat white--text red"
      >
        <span class="font-weight-bold">{{ item.label }}</span>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data: () => ({
    menu: []
  }),
  methods: {
    getMenu () {
      if (this.isLogged()) {
        this.menu = [
          {
            label: 'My Page',
            link: '/personalpage'
          },
          {
            label: 'Ekipazh',
            link: '/ekipazh'
          },
          {
            label: 'Planes',
            link: '/planes'
          },
          {
            label: 'Reys',
            link: '/reys'
          },
          {
            label: 'Tranzit',
            link: '/tranzit'
          },
          {
            label: 'SignOut',
            link: '/signout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Home',
            link: '/'
          },
          {
            label: 'Login',
            link: '/login'
          },
          {
            label: 'Register',
            link: '/register'
          }
        ]
      }
      return this.menu
    },
    isLogged () {
      const token = localStorage.getItem('token')
      return !!token
    }
  },
  created () {
    this.getMenu()
    this.$bus.$on('logged', () => {
      this.getMenu()
    })
  }
}
</script>
