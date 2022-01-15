<template>
  <div class="add">
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    </div>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Enter First name"
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Enter Last name"
            v-model="addForm.last_name"
          />
          <v-select
            label="Choose group"
            v-model="addSub.subject"
            multiple="multiple"
            :items="subjects"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in subjects" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StudentEdit',
  data: () => ({
    t_id: 0,
    t_cur: {
      first_name: '',
      last_name: '',
      room: '',
      subjects: []
    },
    subjects: [],
    addForm: {
      first_name: '',
      last_name: '',
      room: ''
    },
    addSub: {
      subject: []
    }
  }),
  created () {
    this.t_id = this.$route.params.student_id
    this.axios
      .get(`http://127.0.0.1:8000/student/${this.t_id}`)
      .then((res) => {
        console.log(res.data)
        this.t_cur = res.data
        this.addForm.last_name = this.t_cur.last_name
        this.addForm.first_name = this.t_cur.first_name
        this.addForm.room = this.t_cur.room
      })
    this.axios
      .get('http://127.0.0.1:8000/stugroup/list/')
      .then((res) => {
        for (const i of res.data) {
          if (i.student.toString() === this.t_id) {
            this.t_cur.subjects.push(i.group)
            this.addSub.subject.push(i.group)
          }
        }
        console.log(res.data)
      })
    this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        const data = res.data
        console.log(res.data)
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].name}`
          const id = data[i].id
          this.subjects.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/student/${this.t_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      console.log(this.t_cur)
      for (const sub of this.t_cur.group) {
        console.log(sub)
        const id = await this.axios
          .get('http://127.0.0.1:8000/stugroup/list/')
          .then((res) => {
            console.log(res.data)
            return res.data.filter(val => val.student.toString() === this.t_id && val.group === sub.id)[0].id
          })
          .catch((error) => {
            console.log(error)
          })
        await this.axios
          .delete(`http://127.0.0.1:8000/stugroup/${id}/`)
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      for (const sub of this.addSub.subject) {
        await this.axios
          .post('http://127.0.0.1:8000/stugroup/create/', {
            student: this.t_id,
            group: sub
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      await this.$router.push('/student')
    }
  }
}
</script>
