<template>
  <div>
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>Skills</v-data-table-header>
      <tr>
        <td><strong>title</strong></td>
        <td><strong>description</strong></td>
      </tr>
      <tr v-for="profession in Professions" :key="profession.id">
        <td>{{ profession.title }}</td>
        <td>{{ profession.description }}</td>
        
      </tr>
      <v-row>
        <v-text-field
            label="Enter profession title"
            v-model="profession.title"
        />
        <v-text-field
            label="Enter profession description"
            v-model="profession.description"
        />
        <td><v-btn @click="createElem()" style="margin-right: 20px">create</v-btn></td>
      </v-row>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Professions',
  data: () => ({
    Professions: [],
    profession: {
        title: '',
        description: '',
    },
    }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/war/professions/')
      .then((res) => {
        this.Professions = res.data.Professions
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async createElem () {
      await this.axios
        .post(`http://127.0.0.1:8000/war/profession/create/`, this.profession)
        .then((res) => {
      console.log(res)
      this.$refs.skill.profession.reset()
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
    text-align: left;
    padding: 0.5rem;
  }
</style>
