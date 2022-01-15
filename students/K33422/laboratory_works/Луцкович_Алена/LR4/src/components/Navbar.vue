<template>
  <nav>
    <v-toolbar class="orange">
      <v-toolbar-title>
        <span class="font-weight-bold white--text">AIRPORT</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
          v-for="item in menu"
          :key="item"
          :to="item.link"
          class="v-toolbar--outlined white--text orange"
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
            label: 'Home Page',
            link: '/home'
          },
          {
            label: 'Airplanes',
            link: '/airplanes'
          },
          {
            label: 'Schedule',
            link: '/schedule'
          },
          {
            label: 'Transits',
            link: '/transits'
          },
          {
            label: 'Administration',
            link: '/administration'
          },
          {
            label: 'Log Out',
            link: '/logout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Log in',
            link: '/login'
          },
          {
            label: 'Sign Up',
            link: '/signup'
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
