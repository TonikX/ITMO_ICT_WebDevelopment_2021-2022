<template>
  <div>
    <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
    <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/mark/create")' elevation="4">Create mark</v-btn>
    <v-simple-table>
      <h2>Marks</h2>
      <tr>
        <td><strong>Student</strong></td>
        <td><strong>Subject</strong></td>
        <td><strong>Mark</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="elem in elems" :key="elem.id" >
        <td>{{ elem.student }}</td>
        <td>{{ elem.subject }}</td>
        <td>{{ elem.mark }}</td>
        <td><v-btn small @click='$router.push(`/mark/${ elem.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(elem.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'MarkCreate',
  data: () => ({
    elems: [],
    marks: [],
    students: [],
    subjects: []
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/mark/list/')
      .then((res) => {
        console.log('this.marks', this.marks)
        this.marks = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        console.log('this.students', res.data)
        this.students = res.data
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
    for (const i of this.marks) {
      const st = this.students.filter(val => val.id === i.student)[0]
      const sub = this.subjects.filter(val => val.id === i.subject)[0]
      this.elems.push({ id: i.id, mark: i.mark, student: `${st.first_name} ${st.last_name}`, subject: sub.name })
    }
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/mark/${elem}`)
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
