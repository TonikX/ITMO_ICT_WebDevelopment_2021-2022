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
     <v-row class="mx-3.5">
     <v-col cols="4" class="mx-auto">
         <div v.else v-for="book in books" :key="book.id">
          <v-card v-if="book.user==userid"
         elevation="2"
         class="px-6 py-5"
         color="black"
         dark
         >
         <div> {{ book.book.name }} </div>
         <br><br>
         <v-btn @click="detailBook(book.book.id)"> Learn more about this book </v-btn><br><br>
         <v-btn @click="returnBook(book.id)"> Return this book </v-btn><br><br>
        </v-card><br>
        </div>
     </v-col>
   </v-row>
  </v-app>
 </section>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Book',
  data () {
    return {
      books: '',
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
    this.loadBook()
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
    gohome () {
      this.$router.push({ name: 'Home' })
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
    loadBook () {
      $.ajax({
        url: 'http://127.0.0.1:8000/library/books/given',
        type: 'GET',
        success: (response) => {
          this.books = response
          console.log(this.empty)
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
        }
      })
    },
    detailBook (id) {
      this.$router.push({ name: 'OneBook', params: { id: id } })
    },
    returnBook (id) {
      $.ajax({
        url: 'http://127.0.0.1:8000/library/books/return/' + id,
        type: 'DELETE',
        success: (response) => {
          alert('You have returned a book')
          this.loadBook()
          window.location = '/books/taken/' + this.userid
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
        }
      })
    }
  }
}
</script>

<style>
h1
{
font-size: 200%;
}
</style>
