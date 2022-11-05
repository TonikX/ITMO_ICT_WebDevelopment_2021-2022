<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <v-container>
    <v-row class="text-center">
      <v-col cols="12">
      </v-col>
      <v-col>
        <v-col>
            <v-btn color=orange @click='$router.push("/AboutView/")'>О нас</v-btn>
        </v-col>
        <v-col>
            <v-btn color=orange @click='$router.push("/candies/")'>Сласти</v-btn>
        </v-col>
                <v-col>
            <v-btn color=orange @click='$router.push("/req/")'>Заказы</v-btn>
        </v-col>
                <v-col>
            <v-btn color=orange @click='$router.push("/sign-up/")'>Сотрудники</v-btn>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
