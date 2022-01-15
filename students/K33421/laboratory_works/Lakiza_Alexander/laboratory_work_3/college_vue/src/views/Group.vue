<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/group/create")' elevation="4">Create group</v-btn>
    </div>
    <v-simple-table>
      <h2>Groups</h2>
      <v-data-table-header>Groups</v-data-table-header>
      <tr>
        <td><strong>Group Name</strong></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in groups" :key="el.id">
        <td>{{ el.name }}</td>
        <td>
          <v-btn small @click='$router.push(`/grouplist/${ el.id }`)' color="primary">Group List</v-btn>
        </td>
        <td>
          <v-btn small @click='$router.push(`/schedule/${ el.id }`)' color="accent">Group Schedule</v-btn>
        </td>
        <td>
          <v-btn small @click='$router.push(`/group/${ el.id }`)'>Edit</v-btn>
        </td>
        <td>
          <v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn>
        </td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'GroupCreate',
  data: () => ({
    groups: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        this.groups = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/group/${elem}`)
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
  text-align: center;
  padding: 0.5rem;
}
</style>
