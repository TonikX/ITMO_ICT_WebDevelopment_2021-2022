<template>
   <b-col cols="6" class="mx-auto border p-3 rounded">
      <sign-in-form />
   </b-col>
</template>

<script>
   import SignInForm from '@/components/auth/SignInForm.vue'

   export default {
      name: "SignInPage",
      components: { SignInForm }
   }
</script>

<style scoped>

</style>