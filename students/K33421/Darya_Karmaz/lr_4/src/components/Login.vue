<template>
<div style="text-align: center;">
<v-app>
    <v-app-bar
      app
      color='black'
      dark
    >
    <v-btn @click="gohome()"
        text
      >
        <span class="mr-2">Home</span>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn v-if="!auth" @click="goSignin()"
        text
      >
        <span class="mr-2">Sign in</span>
      </v-btn>
    </v-app-bar>
  <br><br><br><br>
  <input v-model="login" placeholder="Login"/>
  <input v-model="password" type=password placeholder="Password"/>
  <button @click="setLogin">Enter</button>
</v-app>
</div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Login',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    goSignin () {
      this.$router.push({ name: 'SignIn' })
    },
    gohome () {
      this.$router.push({ name: 'Home' })
    },
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push({ name: 'Home' })
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Login or password are incorrect')
          }
        }
      })
    }
  }
}
</script>

<style>
</style>
