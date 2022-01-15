<template>
  <div class="signup">
    <v-form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Choose type"
            v-model="signUpForm.type"
            :items="types">
          </v-select>
          <v-text-field
            label="Enter first_name"
            v-model="signUpForm.first_name"
          />
          <v-text-field
            label="Enter last_name"
            v-model="signUpForm.last_name"
          />
          <v-text-field
            label="Enter username"
            v-model="signUpForm.username"
          />
          <v-text-field
            label="Enter password"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn color="primary" @click="signUp">Sign Up</v-btn>

          <p class="mt-5">Already registered?
            <router-link to="/signin">Sign In</router-link>
          </p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data: () => ({
    types: ['deputy', 'manager'],
    signUpForm: {
      type: '',
      first_name: '',
      last_name: '',
      username: '',
      password: ''
    }
  }),
  methods: {
    async signUp () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/signin'
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
