/* eslint-disable camelcase */
<template>
  <v-form>
    <v-container>
      <v-card>
        <v-card-title>Add a member to the climbing</v-card-title>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="selected_climbing"
              :items="climbings"
              item-value="id"
              item-text="text"
              outlined
              label="Climbing"
            ></v-select> </v-col
        ></v-row>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="selected_climber"
              :items="climbers"
              item-value="id"
              item-text="full_name"
              outlined
              label="Climber"
            ></v-select> </v-col></v-row>
        <v-row justify="space-around"
          ><v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text" @click="postParticipation"
            >Create</v-btn
          ></v-row>
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreateParticipation',
  data: () => ({
    selected_climbing: null,
    selected_climber: null,
    climbings: [],
    climbers: [],
    peaks: {}
  }),
  methods: {
    getContext () {
      this.axios.get('//127.0.0.1:8000/trip/').then((response) => {
        console.log(response, 'climbings')
        this.climbings = response.data
      })
      this.axios.get('//127.0.0.1:8000/climbers/').then((response) => {
        console.log(response, 'climbers')
        this.climbers = response.data
      })
      this.axios.get('//127.0.0.1:8000/peaks/').then((response) => {
        console.log(response, 'peaks')
        response.data.forEach((peak) => {
          this.peaks[peak.id] = peak.name + ' ('
        })
        this.climbings.forEach((climbing) => {
          console.log(climbing)
          climbing.text =
            this.peaks[climbing.peak] +
            climbing.start_time.replace(/T.*Z/, '').split('-').reverse().join('.') + ' - '
          if (climbing.finish_time != null) {
            climbing.text =
              climbing.text +
              climbing.finish_time.replace(/T.*Z/, '').split('-').reverse().join('.') + ')'
          } else {
            climbing.text += ')'
          }
        })
        this.climbers.forEach((climber) => {
          climber.full_name = climber.first_name + ' ' + climber.last_name
        })
      })
    },
    postParticipation () {
      const part_obj = {
        participant: this.selected_climber.id,
        climbing: this.selected_climbing.id
      }
      console.log(part_obj)
      this.axios
        .post('//127.0.0.1:8000/members/create', part_obj)
        .then((response) => {
          if (response.status === 201) {
            window.location = '/'
          }
        })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
