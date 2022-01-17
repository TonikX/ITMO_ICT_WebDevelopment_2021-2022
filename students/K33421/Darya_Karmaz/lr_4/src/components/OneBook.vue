<template>
 <section>
 <v-app>
    <v-app-bar
      app
      color="black"
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
     <v-row class="mx-2 align-center">
     <v-col class="mx-auto align-centre">
<br><br><br>
          <v-card
         elevation="2"
         class="py-10"
         color="black"
         dark
         >
         <div> <b>Title:</b> {{ book.name }} <br>
          <b>Author:</b> {{ book.author.name }}<br>
          <b>Publisher:</b> {{ book.publisher.name }}<br>
          <b>Year:</b> {{ book.year }}<br>
          <b>Section:</b> {{ book.section.name }}<br>
         </div>
         <br><br>
         <v-btn v-if="auth" @click="takeBook(book.id)"> Take this book </v-btn>
         <v-btn @click="back()"> Back </v-btn>
        </v-card><br>
     </v-col>
   </v-row>
  </v-app>
 </section>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'OneBook',
  data () {
    return {
      book: '',
      userid: ''
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
  created () {
    if (sessionStorage.getItem('auth_token')) {
      $.ajaxSetup({
        headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.findUser()
    }
    this.loadBook(window.location.pathname)
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
    takeBook (book) {
      $.ajax({
        url: 'http://127.0.0.1:8000/library/books/take',
        type: 'POST',
        data: {
          book: book,
          user: this.userid
        },
        success: (response) => {
          alert('You have taken a book')
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
        }
      })
    },
    loadBook (id) {
      $.ajax({
        url: 'http://127.0.0.1:8000/library' + id,
        type: 'GET',
        success: (response) => {
          this.book = response
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
          console.log(response)
        }
      })
    },
    back () {
      history.go(-1)
    },
    gohome () {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style>
h1
{
font-size: 200%; /* Размер шрифта в процентах */
}
</style>
