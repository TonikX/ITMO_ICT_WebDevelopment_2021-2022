<template>
  <div class="signup">
    <v-form
        @submit.prevent="signUp"
        ref="signUpForm"
        class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
              label="Username"
              v-model="signUpForm.username"
          />
          <v-text-field
              label="Password"
              v-model="signUpForm.password"
              type="password"
          />
          <v-text-field
              label="Full name"
              v-model="signUpForm.full_name"
          />
          <v-text-field
              label="Email"
              v-model="signUpForm.email"
          />
          <v-text-field
              label="Experience"
              v-model="signUpForm.experience"
          />

          <v-btn type="submit" color="red" dark>Sign up</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUp',
  data: () => ({
    signUpForm: {
      email: '',
      experience: '',
      full_name: '',
      username: '',
      password: ''
    }
  }),
  methods: {
    async signUp () {
      try {
        const response = await axios
            .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.signUpForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

<style scoped>
</style>
