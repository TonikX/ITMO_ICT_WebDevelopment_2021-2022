<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3">

        <a class="navbar-brand" href="#">
        AdvertAgency
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
            <li class="nav-item"><router-link :to = "{ name:'workers' }">Workers</router-link></li>
            <li class="nav-item"><router-link :to = "{ name:'applications' }">Applications</router-link></li>
            <li class="nav-item"><router-link :to = "{ name:'assignments' }">Aassignments</router-link></li>
            <li class="nav-item"><router-link :to = "{ name:'posts' }">Services</router-link></li>
            <li id="login" class="nav-item"><router-link :to = "{ name:'login' }">Login</router-link></li>
            <li class="nav-item"><router-link :to = "{ name:'logout' }">Logout</router-link></li>
            <li id="sup" class="nav-item"><router-link :to = "{ name:'register' }">Sign up</router-link></li>
            <li id="ch_pass" class="nav-item"><router-link :to = "{ name:'change_password' }">Change password</router-link></li>

          </ul>
        </div>

      </div>
    </nav>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: 'Navbar',
    computed: mapState(['accessToken'])
  }
</script>

<style scoped>
    a {
      color:#000;
  }
    .nav-item {
      padding-right: 20px;
  }
  #login {
    padding-left: 350px;
  }
  #ch_pass{
    width: 200px;
  }
  #sup{
    width: 80px;
  }
</style>
