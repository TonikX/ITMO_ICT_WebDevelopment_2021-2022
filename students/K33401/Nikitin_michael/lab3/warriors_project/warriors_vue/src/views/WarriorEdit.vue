<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Enter race"
            item-text = 'this.warrior_cur.race'
            v-model="addForm.race"
          />
          <v-text-field
            label="Enter name"
            v-model="addForm.name"
          />
          <v-text-field
            label="Enter profession"
            v-model="addForm.profession"
          />
          <v-text-field
            label="Enter level"
            v-model="addForm.level"
          />
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'WarriorEdit',
  data: () => ({
    warrior_id: 0,
    warrior_cur: {},
    addForm: {
      race: '',
      name: '',
      level: '',
      profession: '',
    }
  }),
  created () {
    this.warrior_id = this.$route.params.warrior_id
    this.axios
      .get(`http://127.0.0.1:8000/war/warrior/${this.warrior_id}`)
      .then((res) => {
        console.log(res)
        this.warrior_cur = res.data
        this.addForm.race = this.warrior_cur.race
        this.addForm.name = this.warrior_cur.name
        this.addForm.level = this.warrior_cur.level
        this.addForm.profession = this.warrior_cur.profession
        console.log(this.warrior_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .patch(`http://127.0.0.1:8000/war/warrior/${this.warrior_id}/update/`, this.addForm)
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
