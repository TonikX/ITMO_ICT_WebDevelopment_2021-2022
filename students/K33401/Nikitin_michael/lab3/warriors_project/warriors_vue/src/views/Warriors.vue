<template>
  <div>
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>Warriors</v-data-table-header>
      <tr>
        <td><strong>race</strong></td>
        <td><strong>name</strong></td>
        <td><strong>level</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="warrior in Warriors" :key="warrior.id">
        <td>{{ warrior.race }}</td>
        <td>{{ warrior.name }}</td>
        <td>{{ warrior.level }}</td>
        <td><v-btn small @click='$router.push(`/warrior/${ warrior.id }`)'>show warrior</v-btn></td>
        <td><v-btn small @click='$router.push(`/warrior/edit/${ warrior.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(warrior.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Warriors',
  data: () => ({
    Warriors: [],
    }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/war/warriors/')
      .then((res) => {
        this.Warriors = res.data.Warriors
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (warrior) {
      await this.axios
        .delete(`http://127.0.0.1:8000/war/warrior/${warrior}`)
        .then((res) => {
      console.log(res)
      this.$router.go(0)
      })
      .catch((error) => {
      console.log(error)
      })
    }

    
  }
}
</script>

<style>
  table {
    margin-top: 50px;
    width: 100%;
  }
  td {
    text-align: left;
    padding: 0.5rem;
  }
</style>
