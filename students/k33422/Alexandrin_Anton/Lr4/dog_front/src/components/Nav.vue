<template>
  <nav>
    <v-toolbar class="black">
      <v-toolbar-title>
        <span class="white--text">Dog shows</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
          v-for="item in menu"
          :key="menu.item"
          :to="item.link"
          class="float-left v-toolbar--flat white--text blue darken-4 "


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
            label: 'Profile',
            link: '/profile'
          },
          {
            label: 'Experts',
            link: '/experts'
          },
          {
            label: 'Participants',
            link: '/participants'
          },
          {
            label: 'Report',
            link: '/report'
          },
          {
            label: 'Misc',
            link: '/misc'
          },
          {
            label: 'Log out',
            link: '/logout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Home',
            link: '/'
          },
          {
            label: 'Log in',
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