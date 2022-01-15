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
          <v-select
            label="Choose student"
            v-model="addForm.student"
            @click="getStudent"
            :items="students"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="st in students" :key="st.id">
              {{ st.label }}
            </option>
          </v-select>
          <v-select
            label="Choose subject"
            v-model="addForm.subject"
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
            label="Enter mark"
            v-model="addForm.mark"
          />
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'MarkCreate',
  data: () => ({
    students: [],
    subjects: [],
    addForm: {
      student: '',
      subject: '',
      group: ''
    }
  }),
  methods: {
    async getStudent () {
      await this.axios
        .get('http://127.0.0.1:8000/student/list/')
        .then((res) => {
          const data = res.data
          for (let i = 0; i < res.data.length; i++) {
            const label = `${data[i].first_name} ${data[i].last_name} ${data[i].group[0].name}`
            const id = data[i].id
            this.students.push({ label: label, code: id })
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
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
        .post('http://127.0.0.1:8000/mark/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/mark')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
