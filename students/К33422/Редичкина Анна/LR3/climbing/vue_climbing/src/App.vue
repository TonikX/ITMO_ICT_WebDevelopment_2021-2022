<template>
  <v-app >
    <v-navigation-drawer dark color="#263238" v-model="drawer" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Climbing club
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
     <v-divider></v-divider>
      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-sheet
      class="overflow-y-auto"
      max-height="1009">
      <v-container>
        <v-main>
          <router-view>
          </router-view>
        </v-main>
      </v-container>
    </v-sheet>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    items: [
      { title: 'Home', icon: 'mdi-home', to: '/' },
      { title: 'My account', icon: 'mdi-account', to: '/account' }
    ]
  })
}
</script>
<style>
.mb-footer {
  margin-bottom: 190px;
}
</style>
