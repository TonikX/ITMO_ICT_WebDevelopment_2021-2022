<template>
  <div id="app" class="body-patch">
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>

import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  name: 'App',
  components: {Footer, Header},
}
</script>

<style>

</style>
