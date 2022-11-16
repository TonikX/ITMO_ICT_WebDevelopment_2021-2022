<template>
  <v-container>
    <v-row>
      <template v-for="(peak, n) in peaks">
        <v-col :key="n">
          <v-card class="pa-2 mb-5" min-height="170">
            <v-card-title>{{
              peak.name + " - " + peak.height + " м."
            }}</v-card-title>
                         <v-divider></v-divider>
            <v-card-subtitle>{{ peak.country }}</v-card-subtitle>
            <v-card-subtitle>{{ peak.route_description }}</v-card-subtitle>
          </v-card>
        </v-col>
        <v-responsive
          v-if="(n + 1) % 2 === 0"
          :key="`width-${n}`"
          width="100%"
        ></v-responsive>
      </template> </v-row
    ><v-row justify="space-around">
      <v-btn :to="getBtnLink" large color="blue-grey darken-2" class="mb-footer white--text">{{
        getBtnName
      }}</v-btn></v-row>
  </v-container>
</template>
<script>
import UpdatePeak from './UpdatePeak.vue'
export default {
  name: 'PeakList',
  component: { UpdatePeak },
  data: () => ({
    show: false,
    peaks: []
  }),
  computed: {
    getBtnName: function () {
      if (this.$route.path.includes('no_trips')) {
        return 'View full list'
      }
      return 'View list without climbings'
    },
    getBtnLink: function () {
      if (this.$route.path.includes('no_trips')) {
        return '/peaks/'
      }
      return '/peaks/no_trips'
    }
  },
  mounted () {
    this.getContext()
    console.log(this.$route)
  },
  updated () {
    this.getContext()
  },
  methods: {
    getContext () {
      this.axios.get('//127.0.0.1:8000' + this.$route.path)
        .catch(function (error) {
          if (error.response) {
            console.log(error.response.status)
          } else {
            console.log('Error', error.message)
          }
        })
        .then((response) => {
          console.log(response.data)
          this.peaks = response.data
        })
      console.log(this.peaks)
    }
  }
}
</script>
