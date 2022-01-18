<template>
  <div class="signin">
    <v-form
      @submit.prevent="signIn"
      ref="signInForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter username"
            v-model="signInForm.username"
          />
          <v-text-field
            label="Enter password"
            v-model="signInForm.password"
            type="password"
          />
          <v-btn color="primary" @click='signIn'>Sign In</v-btn>

          <p class="mt-5">Don't have an account yet?
            <router-link to="/signup">Sign Up</router-link>
          </p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignIn',
  data: () => ({
    signInForm: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async signIn () {
      const token = await this.axios
        .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        .then((res) => {
          console.log(res)
          return res.data.auth_token
        })
        .catch((error) => {
          console.log(error)
          alert('Invalid username or password!')
        })
      localStorage.setItem('token', token)
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
      const userType = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/')
        .then((res) => {
          console.log(res.data)
          return res.data
        })
      if (userType.type === 'manager') {
        window.location.href = 'http://localhost:8080/manager'
      } else if (userType.type === 'deputy') {
        window.location.href = 'http://localhost:8080/deputy'
      }
    }
  }
}
</script>
