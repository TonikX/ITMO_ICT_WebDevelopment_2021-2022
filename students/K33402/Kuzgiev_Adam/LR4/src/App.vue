<template>
    <v-app>
      <Header @openSnackbar="openSnackbar"></Header>
      <v-main>
        <v-container>
          <router-view></router-view>
        </v-container>
      </v-main>
      <div>
        <v-snackbar
                right
                :color="snackbarData.color"
                v-model="snackbar"
                v-if="snackbarData.text"
        >
          {{ snackbarData.text }}
          <template v-slot:action="{ attrs }">
            <v-btn
                    text
                    v-bind="attrs"
                    @click="snackbar=false"
            >
              Close
            </v-btn>
          </template>
        </v-snackbar>
      </div>
    </v-app>
</template>

<script>
import Header from "@/components/Header.vue"

export default {
  name: 'App',
  components: {
    Header
  },
  data() {
    return {
      snackbar: true,
      snackbarData: {},
    };
  },
  methods: {
    openSnackbar(data = {color: 'primary', text: ''}) {
      this.snackbarData = data
      this.snackbar = true
    }
  },
  mounted() {
    if (Object.keys(this.$store.state.location).length === 0) {
      this.$store.dispatch('ADD_LOCATION')
    } else {
      this.$store.dispatch('ADD_LOCAL_WEATHER')
    }
    this.$store.dispatch('GET_USER')
  }

}
</script>

<style>

</style>
