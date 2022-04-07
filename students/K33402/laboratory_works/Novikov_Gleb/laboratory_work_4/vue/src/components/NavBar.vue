<template>
    <div class="container flex-wrap">
        <nav class="navbar navbar-expand-lg navbar-light bg-light mt-3 mb-5">
            <div class="container-fluid">
              <router-link class="navbar-brand" :to="{name: 'Weather'}">🗿<b> Яндекс.Погода</b></router-link>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarMy">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'Weather'}">| 🌥️ Погода |</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'Profile'}">| 👤 Профиль |</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link class="nav-link" :to="{name: 'SignIn'}">| 🚪 Выход |</router-link>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
    </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>
