<template>
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-card>
          <nav-drawer v-if='auth'/>
        </v-card>
      </v-col>

      <v-col cols="10">
        <v-card>
          <h3>4</h3>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
export default {
  name: 'About',
  components: {
    NavDrawer
  },
  computed: {
    auth () {
      if (localStorage.getItem('token')) {
        return true
      } else {
        return false
      }
    }
  }
}

</script>

<style scoped>

</style>
