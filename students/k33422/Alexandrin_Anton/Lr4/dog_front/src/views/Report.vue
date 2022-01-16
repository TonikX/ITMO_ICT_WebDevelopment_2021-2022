<template>
  <div class="center">

    <v-form
        @submit.prevent="submitID"
    >
      <v-text-field
          label="Year"
          v-model="year"
          type="number"
      />
      <v-btn type="submit" color="black" dark>Show</v-btn>

    </v-form>

    <br/>

    <div v-if="report.participant_count">
      <ul>
        <li>
          Participants count: {{ report.participant_count }}
        </li>
        <li>
          Most popular breed: {{ report.breeds[0].breed }}, {{ report.breeds[0].count }}
        </li>
        <li>
          Best grades: {{ report.best_grades }}
        </li>
        <li>
          Medals: {{ report.medals[0].breed }}, {{ report.medals[0].medals_count }}
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import axios from "axios";

const host = 'http://127.0.0.1:8000'

export default {
  name: "Report",

  data: () => ({
    year: null,
    savedYear: null,
    report: {
      "participant_count": null,
      "breeds": [
        {
          "breed": null,
          "count": null
        }
      ],
      "best_grades": [],
      "medals": [
        {
          "breed": null,
          "medals_count": null
        }
      ]
    }
  }),

  methods: {
    async submitID() {
      this.savedYear = parseInt(this.year)
      try {
        const response = await axios
            .get(`${host}/report/` + JSON.stringify(this.savedYear))
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.report = response.data
        return response.data
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
  }
}
</script>

<style scoped>

</style>