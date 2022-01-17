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
    <v-btn v-if="!auth" @click="goLogin()"
        text
      >
        <span class="mr-2">Login</span>
      </v-btn>
    </v-app-bar>
  <br><br><br><br>
  <input v-model="login" placeholder="Login"/>
  <input v-model="first_name" placeholder="First Name"/>
  <input v-model="last_name" placeholder="Last Name"/>
  <input v-model="tel" placeholder="Phone Number"/>
  <input v-model="password" type=password placeholder="Password"/>
  <button @click="register">Enter</button>
</v-app>
</div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'SignIn',
  data () {
    return {
      login: '',
      password: '',
      first_name: '',
      last_name: '',
      tel: ''
    }
  },
  methods: {
    goLogin () {
      this.$router.push({ name: 'Login' })
    },
    gohome () {
      this.$router.push({ name: 'Home' })
    },
    register () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name,
          tel: this.tel
        },
        success: (response) => {
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push({ name: 'Home' })
        },
        error: (response) => {
          if (response.status === 400) {
            if (this.password === '') {
              alert('Password is required')
            } else if (this.login === '') {
              alert('Username is required')
            } else {
              alert('A user with this username already exists')
            }
          }
        }
      })
    }
  }
}
</script>

<style>
</style>
