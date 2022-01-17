<template>
  <v-card class="center">
    <v-container v-if="mytoken != null"
      ><v-card-title>My account info</v-card-title>
    </v-container>
    <v-form v-if="mytoken != null" class="mb-footer"
      ><v-row justify="center"
        ><v-col cols="10">
          <v-text-field
            readonly
            v-model="username"
            label="Username"
            :rules="[rules.required]"
          >
          </v-text-field></v-col
        >
        <v-col cols="10">
          <v-text-field
            v-model="email"
            label="E-mail"
            placeholder="mymail@mail.com"
            :rules="[rules.required]"
          >
          </v-text-field></v-col
        >
      </v-row>
      <v-row justify="center">
        <v-btn large  color="blue-grey darken-2"  class="my-5 mr-5 white--text" @click="saveAccount"
          >Update your account</v-btn
        ><v-btn large color="blue-grey darken-2" class="my-5 white--text" @click="logout"
          >Log out</v-btn
        ></v-row
      >
    </v-form>
    <v-container v-if="mytoken == null">
    <v-card-actions class="justify-center">
        <v-btn block x-large color="blue-grey darken-2" class="text-center white--text" elevation="13" to="account/register"
          >Sign up</v-btn>
        </v-card-actions>
    <v-card-actions class="justify-center">
        <v-btn block x-large color="blue-grey darken-2" class="text-center white--text" elevation="13" to="account/login"
          >Login</v-btn>
       </v-card-actions>
      </v-container>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    mytoken: null,
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    rules: {
      required: (value) => !!value || 'Required.'
    }
  }),
  mounted () {
    this.mytoken = sessionStorage.getItem('auth_token')
    if (this.mytoken != null) {
      console.log('Token ' + this.mytoken)
      this.axios
        .get('//127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: 'Token ' + this.mytoken
          }
        })
        .then((response) => {
          console.log(response)
          this.username = response.data.username
          this.email = response.data.email
        })
    }
  },
  methods: {
    logout () {
      console.log(this.mytoken)
      sessionStorage.removeItem('auth_token')
      this.mytoken = null
      console.log(this.mytoken)
      window.location = '/account'
    },
    saveAccount () {
      console.log('save changes')
      this.axios
        .patch(
          '//127.0.0.1:8000/auth/users/me/',
          { email: this.email },
          {
            headers: {
              Authorization: 'Token ' + this.mytoken
            }
          }
        )
        .then((response) => {
          if (response.status === 200) {
            alert('success!')
          }
        })
    }
  }
}
</script>
