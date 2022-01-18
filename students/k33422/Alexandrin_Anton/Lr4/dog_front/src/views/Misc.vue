<template>
  <div class="center">
    <h3>Which experts judge breeds?</h3>
    <br/>
    <ul>
      <li
          v-for="item in breedExperts"
          :key="item.id"
      >
        {{ item.breed }}: {{ item.experts.map(exp => `${exp.name} ${exp.last_name}`).join(', ') }}

      </li>
    </ul>

    <br/>
    <h3>How many dogs of each breed there is?</h3>
    <br/>
    <ul>
      <li
          v-for="item in breedCount.breed_count"
          :key="item.id"
      >
        {{ item.breed }}: {{ item.count }}
      </li>
    </ul>

  </div>

</template>

<script>
import axios from "axios";

const host = 'http://127.0.0.1:8000'

export default {
  name: "Misc",

  data: () => ({
    breedExperts: [],
    breedCount: {}
  }),

  methods: {
    async getBreedExperts() {
      try {
        const response = await axios
            .get(`${host}/breed_experts/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.breedExperts = response.data
        return response.data
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async getBreedsCount() {
      try {
        const response = await axios
            .get(`${host}/breeds_count/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.breedCount = response.data
        return response.data
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
  },
  beforeMount() {
    this.getBreedExperts()
    this.getBreedsCount()
  }
}
</script>

<style scoped>

</style>