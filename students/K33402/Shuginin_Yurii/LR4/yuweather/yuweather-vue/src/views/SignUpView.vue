<template>
  <div class="registration">
    <SimpleHeader />
    <main>
      <div class="container py-4">
        <SignUpForm />
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import SimpleHeader from '@/components/SimpleHeader.vue'
import Footer from '@/components/Footer.vue'
import SignUpForm from '@/components/SignUpForm.vue'

export default {
  name: 'SignUpView',
  components: {
    SimpleHeader,
    Footer,
    SignUpForm
  }
}
</script>
