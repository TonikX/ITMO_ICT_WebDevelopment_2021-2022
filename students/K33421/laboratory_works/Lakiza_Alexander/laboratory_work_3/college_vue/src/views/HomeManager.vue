<template>
  <div>
    <v-btn class="btn" @click="$router.push('/pair/create')">Pair Create</v-btn>
    <v-simple-table>
      <h2>Pairs</h2>
      <v-data-table-header>pairs</v-data-table-header>
      <tr>
        <td><strong>Day's name</strong></td>
        <td><strong>Pair number</strong></td>
        <td><strong>Group</strong></td>
        <td><strong>Subject</strong></td>
        <td><strong>Room</strong></td>
        <td><strong>Teacher</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in elems" :key="el.id">
        <td>{{ el.name_day }}</td>
        <td>{{ el.pair_number }}</td>
        <td>{{ el.group }}</td>
        <td>{{ el.subject }}</td>
        <td>{{ el.room }}</td>
        <td>{{ el.teacher }}</td>
        <td>
          <v-btn small @click='$router.push(`/pair/${ el.id }`)'>Edit</v-btn>
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
  name: 'HomeManager',
  data: () => ({
    pairs: [],
    teachers: [],
    subjects: [],
    groups: [],
    elems: []
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        console.log('this.groups', res.data)
        this.groups = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    for (const i of this.pairs) {
      const gro = this.groups.filter(val => val.id === i.group)[0]
      const tea = this.teachers.filter(val => val.id === i.teacher)[0]
      const sub = this.subjects.filter(val => val.id === i.subject)[0]
      this.elems.push({
        id: i.id,
        pair_number: i.pair_number,
        name_day: i.name_day,
        room: i.room,
        group: gro.name,
        subject: sub.name,
        teacher: `${tea.first_name} ${tea.last_name}`
      })
    }
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/pair/${elem}`)
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

.btn {
  margin-top: 10px;
}
</style>
