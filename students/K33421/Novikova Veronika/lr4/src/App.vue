<template>
  <v-app>
    <v-app-bar
      app
      color="dark"
      dark
    >
      <div class="d-flex align-center">
        <v-toolbar-title>Funny Farm</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
    <v-btn>
      <router-link to="/workerslist">Workers</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/chickenslist">Chickens</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/breedslist">Breeds</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/cageslist">Cages</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/taskslist">Tasks</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/signin">Sign In</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/signup">Sign Up</router-link>
    </v-btn>
    </v-toolbar-items>
    <v-btn icon @click="logout">
          <v-icon>mdi-export</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'App',
  created () {
    if (localStorage.getItem('token')) {
      $.ajaxSetup({
        headers: {
          Authorization: 'Token' + localStorage.getItem('token')
        }
      })
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'SignIn' })
    }
  }
}
</script>
