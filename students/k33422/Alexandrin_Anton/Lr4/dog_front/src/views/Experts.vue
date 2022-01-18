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
          label="Last Name"
          v-model="editedItem.last_name"
      />
      <v-text-field
          label="Club"
          v-model="editedItem.club"
          type="number"
      />
      <v-text-field
          label="Ring"
          v-model="editedItem.ring"
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
  name: "Experts",

  data: () => ({
    ID: null,
    savedID: null,
    editedItem: {
      name: '',
      last_name: '',
      club: null,
      ring: null,
    }
  }),

  methods: {
    async submitID() {
      this.savedID = parseInt(this.ID)
      try {
        const response = await axios
            .get(`${host}/experts/` + JSON.stringify(this.savedID))
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
            .put(`${host}/experts/` + JSON.stringify(this.savedID), this.editedItem
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
            .delete(`${host}/experts/` + JSON.stringify(this.editedItem.id), this.editedItem
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
