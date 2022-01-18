<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/student/create")' elevation="4">Create student</v-btn>
    </div>

    <v-simple-table>
      <h2>Students</h2>
      <v-data-table-header>Students</v-data-table-header>
      <tr>
        <td><strong>Last name</strong></td>
        <td><strong>First name</strong></td>
        <td><strong>Group</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in students" :key="st.id">
        <td>{{ st.last_name }}</td>
        <td>{{ st.first_name }}</td>
        <td><i v-for="sub in st.group" :key="sub.id">{{ sub.name }} </i></td>
        <td><v-btn small @click='$router.push(`/student/${ st.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(st.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data: () => ({
    students: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/student/${st}`)
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
