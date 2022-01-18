<template>
  <div id="app">
    <Navbar/>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Nav";

export default {
  components: {Navbar}
}

</script>

<style>

body {
  font-family: 'Roboto', sans-serif;
}

.content {
  padding: 100px;
}

</style>
