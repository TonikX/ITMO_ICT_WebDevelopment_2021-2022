<template>
    <header v-if="auth()">
        <div class="container d-flex flex-wrap align-items-center justify-content-sm-between justify-content-center border-bottom border-primary py-3">
            <a class="navbar-brand d-flex align-items-center justify-content-center" href="/">
                <img src="@/images/dove.png" alt="" width="35" height="30" class="d-inline-block me-1">
                YuWeather
            </a>

            <ul class="nav nav-pills justify-content-center">
                <li class="nav-item"><a href="favourites" class="nav-link">Favourites</a></li>
                <li class="nav-item"><a href="profile" class="nav-link">Profile</a></li>
                <li class="nav-item"><button type="button" class="btn btn-outline-primary ms-3" data-bs-toggle="modal" data-bs-target="#LogOutModal">Log out</button></li>
            </ul>
        </div>
    </header>
    <header v-else>
        <div class="container d-flex flex-wrap flex-column flex-sm-row align-items-center justify-content-sm-between justify-content-center border-bottom border-primary py-3">
            <a class="navbar-brand d-flex align-items-center justify-content-center" href="/">
                <img src="@/images/dove.png" alt="" width="35" height="30" class="d-inline-block me-1">
                YuWeather
            </a>

            <div class="pt-2 pt-sm-0">
                <a class="btn btn-outline-primary me-2" href="login" role="button">Login</a>
                <a class="btn btn-primary" href="registration" role="button">Sign-up</a>
            </div>
        </div>
    </header>
</template>

<script>
export default {
  name: 'HeaderComponent',

  methods: {
    auth () {
      return localStorage.getItem('token')
    }
  }
}
</script>

<style>
</style>
