<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <HomePage msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HomePage from '@/components/HomePage.vue'
export default {
  name: 'Home',
  components: { HomePage },
  data: () => ({
  })
}
</script>
