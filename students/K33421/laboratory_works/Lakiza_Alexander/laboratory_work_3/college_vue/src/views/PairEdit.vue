<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)'>Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/manager")'>Home</v-btn>
    </div>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-select
            label="Choose group"
            v-model="addForm.group"
            :items="groups"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in groups" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-text-field
            label="Enter pair number"
            v-model="addForm.pair_number"
          />
          <v-select
            label="Choose day"
            v-model="addForm.name_day"
            :items="days">
            <option v-for="st in days" :key="st.id">
              {{ st }}
            </option>
          </v-select>
          <v-text-field
            label="Enter room"
            v-model="addForm.room"
          />
          <v-select
            label="Choose teacher"
            v-model="addForm.teacher"
            :items="teachers"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in teachers" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-select
            label="Choose subject"
            v-model="addForm.subject"
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
  name: 'PairCreate',
  data: () => ({
    st_id: 0,
    st_cur: {},
    pairs: [],
    teachers: [],
    subjects: [],
    groups: [],
    days: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    elems: [],
    addForm: {
      group: '',
      name_day: '',
      pair_number: '',
      room: '',
      teacher: '',
      subject: ''
    }
  }),
  async created () {
    this.st_id = this.$route.params.pair_id
    this.axios
      .get(`http://127.0.0.1:8000/pair/${this.st_id}`)
      .then((res) => {
        this.st_cur = res.data
        this.addForm.pair_number = this.st_cur.pair_number
        this.addForm.group = this.st_cur.group
        this.addForm.teacher = this.st_cur.teacher
        this.addForm.room = this.st_cur.room
        this.addForm.name_day = this.st_cur.name_day
        this.addForm.subject = this.st_cur.subject
        console.log(this.st_cur)
      })
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].first_name} ${data[i].last_name}`
          const id = data[i].id
          this.teachers.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = data[i].name
          const id = data[i].id
          this.groups.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        const data = res.data
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
        .put(`http://127.0.0.1:8000/pair/${this.st_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/manager')
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
