<template>
  <div class="signin">
    <v-form
      @submit.prevent="logIn"
      ref="form"
      class="my-2"
      id="check-login-form"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter password"
            v-model="password"
            type="password"
          />
          <v-text-field
            label="Enter username"
            v-model="username"
          />
          <v-btn type="submit" color="red" dark>Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignIn',
  data: () => ({
    password: null,
    username: null
  }),
  methods: {
    logIn () {
      try {
        this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', {
            password: this.password,
            username: this.username
          }).then(response => { this.setLogIn(response) })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    setLogIn (response) {
      console.log(this.password)
      console.log(this.username)
      localStorage.setItem('token', response.data.auth_token)
      this.$bus.$emit('logged', 'User logged')
      // this.username = ''
      // this.password = ''
      // this.$refs.form.reset()
      this.$router.push('/personalpage')
    }
  }
}
</script>
