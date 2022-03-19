<template>
  <div class="signup">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/")' elevation="4">Отмена</v-btn>
    </div>
    <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Зарегистрироваться</h2>
    <br>
    <v-form
        @submit.prevent="signUp"
        ref="signUpForm"
        class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
              label="Фамилия"
              v-model="signUpForm.last_name"
          />
          <v-text-field
              label="Имя"
              v-model="signUpForm.first_name"
          />
          <v-text-field
              label="Отчество"
              v-model="signUpForm.patronymic"
          />
          <v-text-field
              label="Паспорт"
              v-model="signUpForm.passport"
          />
          <v-text-field
              label="Номер"
              v-model="signUpForm.number"
          />
          <v-text-field
              label="Никнейм"
              v-model="signUpForm.username"
          />
          <v-text-field
              label="Пароль"
              v-model="signUpForm.password"
              type="password"
          />
          <v-btn type="submit" color="orange">ОК</v-btn>
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
      last_name: '',
      first_name: '',
      patronymic: '',
      passport: '',
      number: '',
      username: '',
      password: ''
    }
  }),
  methods: {
    async signUp () {
      try {
        const response = await axios
          .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        window.location.href = 'http://localhost:8080/sign-in/'
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
