<template>
  <div class="center">

    <v-form
        @submit.prevent="submitID"
    >
      <v-text-field
          label="ID"
          v-model="ID"
          type="number"
      />
      <v-btn type="submit" color="black" dark>Show</v-btn>

    </v-form>

    <v-form
        @submit.prevent="changeData"
        v-if="savedID"
    >
      <v-text-field
          label="Name"
          v-model="editedItem.name"
      />
      <v-text-field
          label="Breed"
          v-model="editedItem.breed"
      />
      <v-text-field
          label="Age"
          v-model="editedItem.age"
          type="number"
      />
      <v-text-field
          label="Family"
          v-model="editedItem.family"
      />
      <v-text-field
          label="Vaccinated"
          v-model="editedItem.vaccinated"
      />
      <v-text-field
          label="Owner data"
          v-model="editedItem.owner_data"
      />
      <v-checkbox
          label="Dismissed"
          v-model="editedItem.dismissed"
      />
      <v-text-field
          label="Club"
          v-model="editedItem.club"
      />
      <v-btn type="submit" color="black" dark>Post</v-btn>
    </v-form>

    <v-btn @click="deleteData">Delete</v-btn>

  </div>
</template>

<script>
import axios from "axios";

const host = 'http://127.0.0.1:8000'

export default {
  name: "Participants",

  data: () => ({
    ID: null,
    savedID: null,
    editedItem: {
      name: '',
      breed: '',
      family: '',
      vaccinated: '',
      owner_data: '',
      age: null,
      dismissed: false,
      club: null,
    }
  }),

  methods: {
    async submitID() {
      this.savedID = parseInt(this.ID)
      try {
        const response = await axios
            .get(`${host}/participants/` + JSON.stringify(this.savedID))
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.editedItem = response.data
        return response.data
      } catch (e) {
        console.error('API ERROR', e)
      }
    },

    async changeData() {
      try {
        const response = await this.axios
            .put(`${host}/participants/` + JSON.stringify(this.savedID), this.editedItem
            )
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async deleteData() {
      try {
        const response = await this.axios
            .delete(`${host}/participants/` + JSON.stringify(this.editedItem.id), this.editedItem
            )
        if (response.status !== 200) {
          throw new Error(response.status)
        }
      } catch (e) {
        console.error('API ERROR', e)
      }
    }
  }
}

</script>

<style scoped>

</style>