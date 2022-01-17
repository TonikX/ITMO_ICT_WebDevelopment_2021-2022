<template>
  <v-container>
    <v-row class="mt-5" >
      <v-col cols="9" class="mx-auto ">
        <v-list dark color="#455A64">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Climber</v-list-item-title>
            </template>
            <v-list-item link :href="'climbers'">
              <v-list-item-title>View list</v-list-item-title>
            </v-list-item>
            <v-list-item link :href="'climbers/create'">
              <v-list-item-title>Add new</v-list-item-title>
            </v-list-item>
            </v-list-group>
        </v-list>
      </v-col>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Peak</v-list-item-title>
            </template>
            <v-list-item link :href="'peaks/'">
              <v-list-item-title>View list</v-list-item-title>
            </v-list-item>
            <v-list-item link :href="'peaks/create'">
              <v-list-item-title>Add new</v-list-item-title>
            </v-list-item>
            <v-list-group :value="false" no-action sub-group>
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title
                    >Edit</v-list-item-title
                  > </v-list-item-content>
              </template>
              <v-list-item
                v-for="peak in peaks"
                :key="peak.id"
                link
                :href="peak.route">
                <v-list-item-title>{{
                  peak.name + " (" + peak.height + " м.) - " + peak.country
                }}</v-list-item-title>
              </v-list-item>
            </v-list-group>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Trips</v-list-item-title>
            </template>
            <v-list-item link :href="'trip/'">
              <v-list-item-title>View list</v-list-item-title
              >
            </v-list-item>
            <v-list-item link :href="'trip/create'">
              <v-list-item-title>Add new</v-list-item-title
              >
            </v-list-item>
            <v-list-item link :href="'members/create'">
              <v-list-item-title>Add a participant</v-list-item-title
              >
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
       <v-row>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" class="mb-footer">
          <v-list-item link :href="'emergencies/create'">
            <v-list-item-title>Create an emergency</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HomePage',
  data: () => ({
    climbers: Object,
    peaks: Object
  }),
  mounted () {
    this.getContext()
  },
  methods: {
    getContext () {
      this.axios
        .get('//127.0.0.1:8000/climbers/')
        .catch(function (error) {
          if (error.response) {
            console.log(error.response.status)
          } else {
            console.log('Error', error.message)
          }
        })
        .then((response) => {
          console.log(response.data)
          this.climbers = response.data
          this.climbers.forEach((climber) => {
            climber.route = 'climbers/' + climber.id
          })
        })
        .catch((error) => console.log(error.response.data))
      this.axios
        .get('//127.0.0.1:8000/peaks/')
        .then((response) => {
          console.log(response.data)
          this.peaks = response.data
          this.peaks.forEach((peak) => {
            peak.route = 'peaks/' + peak.id
          })
        })
        .catch((error) => console.log(error.response.data))
    }
  }
}
</script>
