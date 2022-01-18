<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/subject/create")' elevation="4">Create subject</v-btn>
    </div>
    <v-simple-table>
      <h2>Subjects</h2>
      <v-data-table-header>subjects</v-data-table-header>
      <tr>
        <td><strong>Name</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in subjects" :key="st.id">
        <td>{{ st.name }}</td>
        <td><v-btn small @click='$router.push(`/subject/${ st.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(st.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Subject',
  data: () => ({
    subjects: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/subject/${st}`)
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
