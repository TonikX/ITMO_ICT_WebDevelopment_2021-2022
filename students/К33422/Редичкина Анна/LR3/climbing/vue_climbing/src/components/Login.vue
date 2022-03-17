<template>
  <v-card class="mt-5">
    <v-card-title>Login to your personal account</v-card-title>
    <v-form class="mb-footer"
      ><v-row justify="center"
        ><v-col cols="10">
          <v-text-field
            v-model="username"
            label="Username"
            :rules="[rules.required]">
          </v-text-field></v-col>
        <v-col cols="10">
          <v-text-field
            v-model="password"
            :rules="[rules.required, rules.min]"
            :type="show_password ? 'text' : 'password'"
            label="Password"
            @click:append="show_password = !show_password"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-btn large color="blue-grey darken-2"  class="text-center mb-5 white--text" @click="tryLogin"
          >Login</v-btn
        ></v-row>
    </v-form>
  </v-card>
</template>
<script>
export default {
  name: 'Login',
  data: () => ({
    show_password: false,
    username: '',
    password: '',
    rules: {
      required: (value) => !!value || 'Required.',
      min: (v) => v.length >= 8 || 'Min 8 characters'
    }
  }),
  mounted () {},
  methods:
  {
    tryLogin () {
      this.axios
        .post('//127.0.0.1:8000/auth/token/login', {
          username: this.username,
          password: this.password
        })
        .then((response) => {
          console.log(response)
          if (response.status === 200) {
            sessionStorage.setItem('auth_token', response.data.auth_token)
            window.location = '/account'
          }
        })
    }
  }
}
</script>
