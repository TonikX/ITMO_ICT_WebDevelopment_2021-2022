<template>
  <v-form class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Update a peak</v-card-title>

        <v-col>
          <v-text-field
            v-model="peak.name"
            :counter="80"
            label="Peak name"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.country"
            :counter="56"
            label="Country"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>

        <v-col>
          <v-text-field
            v-model="peak.height"
            label="Height in meters"
            :rules="reqRules"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.climbing_duration"
            label="Climbing duration in hours"
            :rules="reqRules"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-textarea
            v-model="peak.route_description"
            clearable
            label="Route description"
          ></v-textarea>
        </v-col>
        <v-row justify="space-around" class="pb-5">
          <v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text" @click="postObj">
            Update
          </v-btn></v-row
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreatePeak',
  mounted () {
    this.getContext()
  },
  data: () => ({
    peak: {
      name: '',
      country: '',
      height: '',
      climbing_duration: '',
      route_description: ''
    },
    reqRules: [(v) => !!v || 'This field is required']
  }),
  methods: {
    getContext () {
      console.log(this.$route)
      this.axios
        .get('//127.0.0.1:8000/peaks/' + this.$route.params.pk)
        .then((response) => {
          console.log(response, 'responce')
          this.peak = response.data
        })
    },
    postObj () {
      console.log(this.peak)
      this.axios
        .put('//127.0.0.1:8000/peaks/' + this.$route.params.pk, this.peak)
        .catch(function (error) {
          if (error.response) {
            console.log(error.response.status)
          } else {
            console.log('Error', error.message)
          }
        })
        .then((response) => {
          console.log(response)
        })
    }
  }
}
</script>
