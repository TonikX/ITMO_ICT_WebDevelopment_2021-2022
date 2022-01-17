<template>
  <v-form class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Create a peak</v-card-title>
        <v-col>
          <v-text-field
            v-model="peak.name"
            label="Peak name"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.country"
            label="Country"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.height"
            label="Height in meters"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.climbing_duration"
            label="Climbing duration in days"
            required
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <v-textarea
            v-model="peak.route_description"
            clearable
            label="Description"
          ></v-textarea>
        </v-col>
        <v-row justify="space-around">
          <v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text"  @click="postObj">
            Создать!
          </v-btn></v-row>
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'CreatePeak',
  data: () => ({
    peak: {
      name: '',
      country: '',
      height: '',
      climbing_duration: '',
      route_description: ''
    }
  }),
  mounted () {},
  methods: {
    postObj () {
      console.log(this.peak)
      this.axios
        .post('//127.0.0.1:8000/peaks/create', this.peak)
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
