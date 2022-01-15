<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/student/create")' elevation="4">Create student</v-btn>
    </div>
    <p></p>
    <span style="font-size:1.3vw"><strong>Group: {{ cur_gr_name }}</strong></span>
    <v-simple-table>
      <v-data-table-header>Group's list of students</v-data-table-header>
      <tr>
        <td><strong>Last name</strong></td>
        <td><strong>First name</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in elems" :key="el.id">
        <td>{{ el.last_name }}</td>
        <td>{{ el.first_name }}</td>
        <td>
          <v-btn small @click='$router.push(`/student/${ el.id }`)'>Edit</v-btn>
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
  name: 'GroupList',
  data: () => ({
    gr_id: 0,
    cur_gr_name: '',
    students: [],
    sortedStudents: [],
    elems: []
  }),
  async created () {
    this.gr_id = this.$route.params.group_id
    console.log(this.gr_id)
    await this.axios
      .get(`http://127.0.0.1:8000/group/${this.gr_id}`)
      .then((res) => {
        console.log(res.data)
        this.cur_gr_name = res.data.name
      })
    await this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    console.log(this.students[0].group[0].id)
    for (const i of this.students) {
      console.log('i', i)
      console.log(this.gr_id)
      if (i.group[0].id.toString() === this.gr_id.toString()) {
        console.log('haha')
        this.elems.push({
          last_name: i.last_name,
          first_name: i.first_name,
          id: i.id
        })
      }
    }
    this.elems.sort(function (a, b) {
      const nameA = a.last_name
      const nameB = b.last_name
      if (nameA < nameB) {
        return -1
      }
      if (nameA > nameB) {
        return 1
      }

      // names must be equal
      return 0
    })
    console.log(this.sortedStudents)
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/student/${elem}`)
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
