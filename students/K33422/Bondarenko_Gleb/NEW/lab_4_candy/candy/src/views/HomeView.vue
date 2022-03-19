<template>
  <div class="home">
        <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
    <img alt="Vue logo" src="../assets/lable.png">
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добро пожаловать в магазин сладостей Конфетное королевство!</h2>
        <v-row>
      <v-col cols="12">
        <div style="text-align: center;">
          <center>
          <v-card color="white" width="1300px"
          elevation="10"
          outlined>
            <v-card-title>
            Наши посетители - взрослые с душой ребёнка. Те люди, что восхищались сладким пиром в Гарри Поттере,
            страстно облизывались при виде фантастических и необыкновенных сладостей Вилли Вонки и мечтали бы попробовать
            волшебный рахат лукум Белой королевы из цикла Хроник Нарнии!
            </v-card-title>
          </v-card>
          <br>
          <v-card color="white" width="1310px"
          elevation="10"
          outlined>
            <v-card-title>
            Потому, ну же - отпустите своего внутреннего ребёнка. Пора бы ему вернуть вас в прошлое, в те волшебные дни
            когда каждая сладость была небывалым чудом.
            </v-card-title>
          </v-card>
          </center>
          <br>
          <h2>Навигация по сайту:</h2></div>
        />
      </v-col>
    </v-row>
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
