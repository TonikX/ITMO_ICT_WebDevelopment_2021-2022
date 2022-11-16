<template>
  <v-form>
    <v-container>
      <v-card>
        <v-card-title>Create an emergency</v-card-title>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="em_obj.climbing"
              :items="climbings"
              item-value="id"
              item-text="text"
              outlined
              label="Climbing"
              @change="updateContext"
            ></v-select> </v-col
        ></v-row>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="em_obj.person"
              :items="current_climbers"
              item-value="id"
              item-text="full_name"
              outlined
              label="Climber"
            ></v-select> </v-col
        ></v-row>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-text-field
              v-model="em_obj.description"
              label="Description"
            ></v-text-field> </v-col
        ></v-row>
        <v-row justify="space-around"
          ><v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text" @click="postEmergency"
            >Create</v-btn
          ></v-row
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreateEmergency',
  data: () => ({
    em_obj: {
      climbing: null,
      person: null,
      description: ''
    },
    climbings: [],
    current_climbers: [],
    climbers: {},
    participations: {},
    peaks: {}
  }),
  methods: {
    getContext () {
      this.axios.get('//127.0.0.1:8000/participations/').then((response) => {
        console.log(response, 'participations')
        response.data.forEach((element) => {
          if (!this.participations[element.climbing]) {
            this.participations[element.climbing] = []
          }
          this.participations[element.climbing].push(element.participant)
        })
      })
      this.axios.get('//127.0.0.1:8000/trip/').then((response) => {
        this.climbings = response.data
      })
      this.axios.get('//127.0.0.1:8000/climbers/').then((response) => {
        this.climbers = response.data
        response.data.forEach((element) => {
          this.climbers[element.id] = element
          this.climbers[element.id].full_name =
            this.climbers[element.id].first_name +
            ' ' +
            this.climbers[element.id].last_name
        })
        console.log(this.climbers, 'climbers')
      })
      this.axios.get('//127.0.0.1:8000/peaks/').then((response) => {
        response.data.forEach((peak) => {
          this.peaks[peak.id] = peak.name + ' ('
        })
        this.climbings.forEach((climbing) => {
          climbing.text =
            this.peaks[climbing.peak] +
            climbing.start_time
              .replace(/T.*Z/, '')
              .split('-')
              .reverse()
              .join('.') +
            ' - '
          if (climbing.finish_time != null) {
            climbing.text =
              climbing.text +
              climbing.finish_time
                .replace(/T.*Z/, '')
                .split('-')
                .reverse()
                .join('.') +
              ')'
          } else {
            climbing.text += ')'
          }
        })
      })
    },
    postEmergency () {
      this.em_obj.climbing = this.em_obj.climbing.id
      this.em_obj.person = this.em_obj.person.id
      console.log(this.em_obj)
      this.axios
        .post('//127.0.0.1:8000/emergencies/create', this.em_obj)
        .then((response) => {
          if (response.status === 201) {
            window.location = '/'
          }
        })
    },
    updateContext () {
      console.log(this.em_obj)
      console.log(this.participations)
      this.em_obj.person = null
      this.current_climbers = []
      this.participations[this.em_obj.climbing.id].forEach((participant) => {
        this.current_climbers.push(this.climbers[participant])
      })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
