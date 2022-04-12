<template>
  <div>
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>Skills</v-data-table-header>
      <tr>
        <td><strong>id</strong></td>
        <td><strong>title</strong></td>
      </tr>
      <tr v-for="skill in Skills" :key="skill.id">
        <td>{{ skill.id }}</td>
        <td>{{ skill.title }}</td>

        
      </tr>
      <v-row>
        <v-text-field
            label="Enter skill title"
            v-model="skill.title"
        />
        <td><v-btn @click="createElem()" style="margin-right: 20px">create</v-btn></td>
      </v-row>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Skills',
  data: () => ({
    Skills: [],
    skill: {
        title: ''
    },
    }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/war/skills/')
      .then((res) => {
        this.Skills = res.data.Skills
        console.log()
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async createElem () {
      await this.axios
        .post(`http://127.0.0.1:8000/war/skill/create/`, this.skill)
        .then((res) => {
      console.log(res)
      this.$refs.skill.reset()
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
    margin-left: 50px;
    width: 80%;
  }
  td {
    text-align: middle;
    padding: 0.5rem;
  }
</style>
