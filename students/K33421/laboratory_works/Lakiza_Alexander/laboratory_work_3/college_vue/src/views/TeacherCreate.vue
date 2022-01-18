<template>
  <div class="add">
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    </div>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter First name"
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Enter Last name"
            v-model="addForm.last_name"
          />
          <v-select
            label="Choose subject"
            v-model="addSub.subject"
            multiple="multiple"
            @click="getSubj"
            :items="subjects"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in subjects" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-text-field
            label="Enter room"
            v-model="addForm.room"
          />
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'TeacherCreate',
  data: () => ({
    teacher_id: '',
    subjects: [],
    addForm: {
      first_name: '',
      last_name: '',
      room: '',
      subjects: {}
    },
    addSub: {
      teacher: '',
      subject: []
    }
  }),
  methods: {
    async getSubj () {
      await this.axios
        .get('http://127.0.0.1:8000/subject/list/')
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
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/teacher/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/teacher/list/')
        .then((res) => {
          this.teacher_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const sub of this.addSub.subject) {
        console.log(sub)
        await this.axios
          .post('http://127.0.0.1:8000/subteach/create/', {
            teacher: this.teacher_id,
            subject: sub
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      await this.$router.push('/teacher')
    }
  }
}
</script>
