<template>
  <div id="app" class="wrapper">
    <Header />
    <main class="">
      <router-view />
    </main>
  </div>
</template>

<script>

import Header from "@/components/Header";
export default {
  name: 'App',
  components: {Header},
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: black;
  }
  #nav a {
    font-weight: bold;
    color: blue;
  }
  main {
    min-height: 600px;
  }
  footer {
    font-size: 20pt;
  }
  footer .jumbotron {
    height: 160px;
  }
</style>
