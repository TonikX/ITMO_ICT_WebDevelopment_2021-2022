<template>
  <div class="login">
    <SimpleHeader />
    <main>
      <div class="container py-4">
        <LoginForm />
      </div>
    </main>
    <Footer :bottom="BottomFooter" />
  </div>
</template>

<script>
import SimpleHeader from '@/components/SimpleHeader.vue'
import Footer from '@/components/Footer.vue'
import LoginForm from '@/components/LoginForm.vue'

export default {
  name: 'LoginView',
  data: () => ({
    BottomFooter: 'bottom'
  }),

  components: {
    SimpleHeader,
    Footer,
    LoginForm
  }
}
</script>
