<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>warrior_cur</v-data-table-header>
      <tr>
        <td><strong>race</strong></td>
        <td><strong>name</strong></td>
    </tr>
   <!--   <td>{{ warrior_cur.race }}</td>
      <td>{{ warrior_cur.name }}</td>
      <td>{{ warrior_cur.level }}</td>
      <td>{{ warrior_cur.profession }}</td>
      <td>{{ warrior_cur.skills }}</td>
    -->    
      <v-row>
        <td><v-btn @click="deleteElem()" style="margin-right: 20px">create</v-btn></td>
      </v-row>
    </v-simple-table>
  </div>
</template>

<<script>
export default {
  name: 'WarriorEdit',
  data: () => ({
    warrior_cur: [],
    warrior: '',
    addForm: []
  }),
  created () {
    this.warrior = 2
    //this.$route.params.warrior_id
    this.axios
      .get(`http://127.0.0.1:8000/war/warrior/${this.warrior}`)
      .then((res) => {
        console.log(res)
        //this.warrior_cur = res.data
        // this.addForm.race = this.warrior_cur.race
        // this.addForm.name = this.warrior_cur.name
        // this.addForm.level = this.warrior_cur.level
        // this.addForm.profession = this.warrior_cur.profession
        // this.addForm.skills = this.warrior_cur.skills
        // 
        //console.log(this.warrior_cur)
      })
  },
  methods: {
      async deleteElem (warrior) {
      await this.axios
        .delete(`http://127.0.0.1:8000/war/warrior/${warrior}`)
        .then((res) => {
      console.log(res)
      this.$router.go(0)
      })
      .catch((error) => {
      console.log(error)
      })
  }
