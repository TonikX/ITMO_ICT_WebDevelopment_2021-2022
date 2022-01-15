<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    </div>
    <v-simple-table>
      <h2>Pairs</h2>
      <v-data-table-header>Pairs</v-data-table-header>
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
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Pair',
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
        console.log('this.teachers', res.data)
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/subject/list')
      .then((res) => {
        console.log('this.subjects', res.data)
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    console.log('this.pairs.length', this.pairs)
    for (const i of this.pairs) {
      console.log('i', i)
      const gro = this.groups.filter(val => val.id === i.group)[0]
      console.log(gro)
      const tea = this.teachers.filter(val => val.id === i.teacher)[0]
      const sub = this.subjects.filter(val => val.id === i.subject)[0]
      this.elems.push({ id: i.id, pair_number: i.pair_number, name_day: i.name_day, room: i.room, group: gro.name, subject: sub.name, teacher: `${tea.first_name} ${tea.last_name}` })
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
