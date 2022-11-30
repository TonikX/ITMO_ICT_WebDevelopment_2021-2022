<template>
  <nav>
    <v-toolbar class="orange">
      <v-toolbar-title>
        <span class="white--text">Warriors</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat white--text orange"
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
    getWar () {
        this.war = [
          {
            label: 'Warriors',
            link: '/warriors'
          },
        ]
      } ,
      return: this.war
  },

  created () {
    this.getWar()
  }
}
</script>
