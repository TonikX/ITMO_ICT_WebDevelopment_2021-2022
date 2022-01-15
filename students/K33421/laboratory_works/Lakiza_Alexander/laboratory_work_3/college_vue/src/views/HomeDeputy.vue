<template>
  <div>
    <v-row>
      <v-col>
        <h3>Students</h3>
        <v-col>
          <v-btn small @click='$router.push("/student")'>Student List</v-btn>
        </v-col>
        <v-col>
          <v-btn small @click='$router.push("/student/create")'>Student Create</v-btn>
        </v-col>
      </v-col>
      <v-col>
        <h3>Teachers</h3>
        <v-col>
          <v-btn small @click='$router.push("/teacher")'>Teacher List</v-btn>
        </v-col>
        <v-col>
          <v-btn small @click='$router.push("/teacher/create")'>Teacher Create</v-btn>
        </v-col>
      </v-col>
      <v-col>
        <h3>Subjects</h3>
        <v-col>
          <v-btn small @click='$router.push("/subject")'>Subject List</v-btn>
        </v-col>
        <v-col>
          <v-btn small @click='$router.push("/subject/create")'>Subject Create</v-btn>
        </v-col>
      </v-col>
      <v-col>
        <h3>Marks</h3>
        <v-col>
          <v-btn small @click='$router.push("/mark")'>Marks List</v-btn>
        </v-col>
        <v-col>
          <v-btn small @click='$router.push("/mark/create")'>Marks Create</v-btn>
        </v-col>
      </v-col>
      <v-col>
        <h3>Groups</h3>
        <v-col>
          <v-btn small @click='$router.push("/group")'>Groups List</v-btn>
        </v-col>
        <v-col>
          <v-btn small @click='$router.push("/group/create")'>Groups Create</v-btn>
        </v-col>
      </v-col>
      <v-col>
        <h3>Pairs</h3>
        <v-col>
          <v-btn small @click='$router.push("/pair")'>Pair List</v-btn>
        </v-col>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'HomeDeputy'
}
</script>
