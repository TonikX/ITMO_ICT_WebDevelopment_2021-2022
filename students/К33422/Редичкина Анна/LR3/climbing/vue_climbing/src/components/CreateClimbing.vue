<template>
  <v-form class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Create a climbing</v-card-title>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="selected_peak"
              :items="peaks"
              item-value="id"
              item-text="name"
              label="Peak"
              outlined
              return-object
              @change="someF()"
            ></v-select
          ></v-col>
        </v-row>
        <v-row justify="space-around">
          <v-col cols="4">
            <v-time-picker
              use-seconds
              v-model="fromtime"
              format="24hr"
              color="blue-grey darken-2"
            ></v-time-picker>
          </v-col>
          <v-col cols="4">
            <v-date-picker v-model="fromdate" color="blue-grey darken-2"></v-date-picker> </v-col
        ></v-row>
        <v-row justify="space-around">
          <v-col cols="4">
            <v-time-picker
              use-seconds
              v-model="totime"
              format="24hr"
              color="blue-grey darken-2"
            ></v-time-picker>
          </v-col>
          <v-col cols="4">
            <v-date-picker v-model="todate" color="blue-grey darken-2"></v-date-picker> </v-col
        ></v-row>
        <v-row justify="space-around">
          <v-col cols="10">
            <v-textarea
              v-model="climbing.information"
              label="Information"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="space-around" class="pb-5">
          <v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text" @click="postObj">
            Create
          </v-btn></v-row
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreateClimbing',
  data: () => ({
    selected_peak: null,
    peaks: Object,
    fromtime: '',
    fromdate: '',
    totime: '',
    todate: '',
    climbing: {
      peak: null,
      start_time: '',
      finish_time: '',
      participants: null,
      information: ''
    },
    reqRules: [(v) => !!v || 'This field is required']
  }),
  mounted () {
    this.getPeaks()
  },
  methods: {
    getPeaks () {
      this.axios.get('//127.0.0.1:8000/peaks/').then((response) => {
        this.peaks = response.data
      })
    },
    postObj () {
      this.climbing.peak = this.selected_peak.id
      this.climbing.start_time = this.fromdate + 'T' + this.fromtime + 'Z'
      this.climbing.finish_time = this.todate + 'T' + this.totime + 'Z'
      this.axios
        .post('//127.0.0.1:8000/trip/create', this.climbing)
        .then((response) => {
          console.log(response)
          if (response.status === 201) {
            window.location = '/'
          }
        })
    }
  }
}
</script>
