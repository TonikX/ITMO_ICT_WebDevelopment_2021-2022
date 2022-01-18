<template>
  <div class="add">
    <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
    <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Enter Group Name"
            item-text='this.gr_cur.name'
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
  name: 'GroupEdit',
  data: () => ({
    gr_id: 0,
    gr_cur: {},
    addForm: {
      name: ''
    }
  }),
  created () {
    this.gr_id = this.$route.params.group_id
    this.axios
      .get(`http://127.0.0.1:8000/group/${this.gr_id}`)
      .then((res) => {
        console.log(res)
        this.gr_cur = res.data
        this.addForm.name = this.gr_cur.name
        console.log(this.gr_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/group/${this.gr_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/group')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
