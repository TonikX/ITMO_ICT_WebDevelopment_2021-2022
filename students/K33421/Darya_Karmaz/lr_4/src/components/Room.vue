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
     <v-row>
     <v-col cols="4" class="mx-auto">
<br><br><br>
         <div v-for="room in rooms" :key="room.id">
          <v-card
         elevation="2"
         class="px-2 py-5"
         color="black"
         dark
         >
         {{ room.name }}<br><br>
         <v-btn @click="oneRoom(room.id)"> Learn more about this room </v-btn>
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
  name: 'Room',
  data () {
    return {
      rooms: ''
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
    }
    this.loadRoom()
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
    loadRoom () {
      $.ajax({
        url: 'http://127.0.0.1:8000/library/rooms/list',
        type: 'GET',
        success: (response) => {
          this.rooms = response
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
          console.log(response)
        }
      })
    },
    oneRoom (id) {
      this.$router.push({ name: 'OneRoom', params: { id: id } })
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
