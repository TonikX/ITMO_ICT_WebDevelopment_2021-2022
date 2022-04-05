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
            label="Email"
            v-model="signUpForm.email"
          />
          <v-text-field
            label="Стаж работы"
            v-model="signUpForm.stajh_raboty"
          />
          <v-text-field
            label="ФИО"
            v-model="signUpForm.fio"
          />
          <v-text-field
            label="Username"
            v-model="signUpForm.username"
          />
          <v-text-field
            label="Пароль"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn type="submit" color="blue" dark>Регистрация</v-btn>
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
      stajh_raboty: '',
      fio: '',
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
