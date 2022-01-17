<template>
  <div>
  <v-app>
   <v-app-bar
      app
      color="black"
      dark
    >
    <v-spacer></v-spacer>
    <v-btn v-if="!auth" @click="goSignin()"
        text
      >
        <span class="mr-2">Sign in</span>
      </v-btn>
      <v-btn v-if="!auth" @click="goLogin()"
        text
      >
        <span class="mr-2">Login</span>
      </v-btn>
      <v-btn v-if="auth" @click="edit()"
        text
      >
        <span class="mr-2">Edit profile</span>
      </v-btn>
      <v-btn v-if="auth" @click="goLogout()"
        text
      >
        <span class="mr-2">Log out</span>
      </v-btn>
    </v-app-bar>
    <br><br><br>
    <v-container>
    <v-row class="text-center">
      <v-col cols="12">
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to our library!
        </h1>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          Here you can:
        </h2>
<br>
        <v-row justify="center">
        <a @click="loadRoom()">
          <h3 class="subheading mx-3">
          See our list of rooms
          </h3>
        </a>
        <a @click="loadBook()">
          <h3 class="subheading mx-3">
          See our list of books
          </h3>
        </a>
        <a v-if="auth" @click="takenBook()">
          <h3 class="subheading mx-3">
          See books that you've taken
          </h3>
        </a>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</v-app>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Home',
  created () {
    if (sessionStorage.getItem('auth_token')) {
      $.ajaxSetup({
        headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.findUser()
    }
  },
  computed: {
    auth () {
      var auth
      if (sessionStorage.getItem('auth_token')) {
        auth = true
      }
      return auth
    }
  },
  data () {
    return {
      rooms: [],
      books: [],
      userid: ''
    }
  },
  methods: {
    goLogin () {
      this.$router.push({ name: 'Login' })
    },
    edit () {
      this.$router.push({ name: 'Edit' })
    },
    goSignin () {
      this.$router.push({ name: 'SignIn' })
    },
    goLogout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/'
    },
    loadRoom () {
      this.$router.push({ name: 'Room' })
    },
    loadBook () {
      this.$router.push({ name: 'Book' })
    },
    findUser () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
        type: 'GET',
        success: (response) => {
          this.userid = response.id
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
        }
      })
    },
    takenBook () {
      this.$router.push({ name: 'TakenBook', params: { id: this.userid } })
    }
  }
}
</script>
