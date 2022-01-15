<template>
  <div class="add">
    <div>
      <v-btn small @click='$router.go(-1)'>Back</v-btn>&nbsp;&nbsp;
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
            label="Enter name"
            item-text = 'this.st_cur.name'
            v-model="addForm.name"
          />
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SubjectEdit',
  data: () => ({
    st_id: 0,
    st_cur: {},
    addForm: {
      name: ''
    }
  }),
  created () {
    this.st_id = this.$route.params.subject_id
    this.axios
      .get(`http://127.0.0.1:8000/subject/${this.st_id}/`)
      .then((res) => {
        this.st_cur = res.data
        this.addForm.name = this.st_cur.name
        console.log(this.st_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/subject/${this.st_id}`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
