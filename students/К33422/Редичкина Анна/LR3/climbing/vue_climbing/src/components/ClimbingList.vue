<template>
  <v-card>
    <v-card-title>Trips</v-card-title>
    <v-data-table
      :headers="headers"
      :items="climbings"
    ></v-data-table>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    peaks: Object,
    climbings: [],
    headers: [
      {
        text: 'Peak name',
        value: 'peak'
      },
      { text: 'Start', value: 'start_time' },
      { text: 'Finish', value: 'finish_time' },
      { text: 'Information', value: 'information' },
      { text: 'Results', value: 'results' }
    ]
  }),
  mounted () {
    this.getPeaks()
    this.getClimbings()
  },
  methods: {
    getPeaks () {
      console.log(this.$route.path)
      this.axios.get('//127.0.0.1:8000/peaks/').then((response) => {
        response.data.forEach((element) => {
          this.peaks[element.id] =
            element.name + ' (' + element.height + ' м.)'
        })
      })
    },
    getClimbings () {
      this.axios
        .get('//127.0.0.1:8000/trip/')
        .then((response) => {
          console.log('route is ', this.$route.fullPath)
          console.log(response.data)
          this.climbings = response.data
          this.climbings.forEach((element) => {
            element.peak = this.peaks[element.peak]
            element.start_time = element.start_time.replace(/T.*Z/, '').split('-').reverse().join('.')
            if (element.finish_time !== null) {
              element.finish_time = element.finish_time.replace(/T.*Z/, '').split('-').reverse().join('.')
            }
          })
          console.log(this.climbings)
        })
    }
  }
}
</script>
