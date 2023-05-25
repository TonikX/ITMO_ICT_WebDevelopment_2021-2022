<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <h3>Вариант 4</h3>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'About',

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
