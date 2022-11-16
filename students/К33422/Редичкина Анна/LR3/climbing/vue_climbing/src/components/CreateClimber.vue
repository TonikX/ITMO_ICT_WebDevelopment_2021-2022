<template>
  <v-form v-model="valid">
    <v-container >
      <v-card class="my-5">
        <v-card-title>Create a climber</v-card-title>
        <v-col>
          <v-text-field
            v-model="first_name"
            label="First name"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="last_name"
            label="Last name"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="address"
            label="Address"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model="club"
            :items="club_names"
            label="Club"
            outlined
          ></v-select>
        </v-col>
        <v-col>
          <v-btn large color="blue-grey darken-2"  class="text-center my-5 mr-5 white--text" @click="postObj">
            Create
          </v-btn></v-col
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreateClimber',
  data: () => ({
    valid: false,
    clubs: Object,
    club_names: [],
    first_name: '',
    last_name: '',
    address: '',
    club: ''
  }),
  mounted () {
    this.getContext()
  },
  methods: {
    getContext () {
      this.axios.get('//127.0.0.1:8000/clubs/').then((response) => {
        console.log(response.data)
        this.clubs = response.data
        this.clubs.forEach((club) => {
          this.club_names.push(club.name)
        })
      })
    },
    postObj () {
      console.log(this.first_name, this.last_name, this.address, this.club)
      let clubid = 0
      this.clubs.forEach((club_obj) => {
        if (club_obj.name === this.club) {
          clubid = club_obj.id
        }
      })
      const obj = {
        first_name: this.first_name,
        last_name: this.last_name,
        address: this.address,
        club: clubid
      }
      console.log(obj)
      this.axios
        .post('//127.0.0.1:8000/climbers/create', obj)
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
