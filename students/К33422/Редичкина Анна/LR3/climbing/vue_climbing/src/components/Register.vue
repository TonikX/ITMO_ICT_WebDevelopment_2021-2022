<template>
  <v-card class="mt-5">
    <v-card-title>Create an account</v-card-title>
    <v-form class="mb-footer"
      ><v-row justify="center"
        ><v-col cols="10">
          <v-text-field
            v-model="username"
            label="Username"
          >
          </v-text-field></v-col
        ><v-col cols="10">
          <v-text-field
            v-model="email"
            label="E-mail"
          >
          </v-text-field
        ></v-col>
        <v-col cols="10">
          <v-text-field
            v-model="password"
            :type="show_password ? 'text' : 'password'"
            label="Password"
            @click:append="show_password = !show_password"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-btn large color="blue-grey darken-2" class="text-center mb-5 white--text" @click="tryRegister"
          >Sign up</v-btn
        ></v-row
      >
    </v-form>
  </v-card>
</template>
<script>
export default {
  name: 'Register',
  data: () => ({
    show_password: false,
    username: '',
    password: '',
    email: ''
  }),
  mounted () {},
  methods: {
    tryRegister () {
      this.axios
        .post('//127.0.0.1:8000/auth/users/', {
          username: this.username,
          password: this.password,
          email: this.email
        })
        .then((response) => {
          console.log(response)
          if (response.status === 201) {
            window.location = '/account/login'
          }
        })
        .catch(error => {
          console.log(error.request._response)
        })
    }
  }
}
</script>
