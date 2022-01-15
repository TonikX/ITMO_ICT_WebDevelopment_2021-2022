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
            label="Enter Group Name"
            v-model="addForm.name"
          />
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'GroupCreate',
  data: () => ({
    addForm: {
      name: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/group/create/', this.addForm)
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
