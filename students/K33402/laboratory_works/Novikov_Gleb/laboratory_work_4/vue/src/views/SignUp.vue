<template>
     <div class="bg">
    <div class="container col-xl-10 col-xxl-8 px-4 py-5">
        <div class="row align-items-center g-lg-5 py-5">
          <div class="col-md-10 mx-auto col-lg-5">
            <h1 class="display-4 fw-bold lh-1 mb-5 center">Регистрация</h1>
            <div class="p-4 p-md-5 border rounded-3 bg-light">
                <b-form @submit.stop.prevent="onSubmit" class="needs-validation">
                  <div  class="mb-4">
                    <b-form-group id="input-group-1" label-for="nickname-input">
                      <b-form-input
                        id="nickname-input"
                        name="nickname-input"
                        v-model="$v.form.nickname.$model"
                        :state="validateState('nickname')"
                        aria-describedby="nickname-input-feedback"
                        placeholder="* Имя пользователя"
                      ></b-form-input>
                      <b-form-invalid-feedback id="nickname-input-feedback">
                        Должно быть более 3 символов.</b-form-invalid-feedback>
                    </b-form-group>
                    </div>
                </b-form>

                <b-form @submit.stop.prevent="onSubmit" class="needs-validation">
                  <div class="mb-4">
                    <b-form-group id="input-group-2" label-for="email-input">
                      <b-form-input
                        id="email-input"
                        name="email-input"
                        v-model="$v.form.email.$model"
                        :state="validateState('email')"
                        type="email"
                        aria-describedby="email-input-feedback"
                        placeholder="* E-mail"
                      ></b-form-input>
                      <b-form-invalid-feedback
                        id="email-input-feedback"
                      >Некоректный E-mail.</b-form-invalid-feedback>
                    </b-form-group>
                    </div>
                </b-form>

                <b-form @submit.stop.prevent="onSubmit" class="needs-validation">
                  <div class="mb-4">
                    <b-form-group id="input-group-3" label-for="password-input">
                      <b-form-input
                        id="password-input"
                        name="password-input"
                        v-model="$v.form.password.$model"
                        :state="validateState('password')"
                        type="password"
                        aria-describedby="password-input-feedback"
                        placeholder="* Пароль"
                      ></b-form-input>
                      <b-form-invalid-feedback
                        id="password-input-feedback"
                      >Должно быть не менее 8 символов.</b-form-invalid-feedback>
                    </b-form-group>
                    </div>
                </b-form>

                <b-form @submit.prevent="onSubmit" class="needs-validation">
                  <div class="mb-4">
                    <b-form-group id="input-group-3" label-for="confirm-password-input">
                      <b-form-input
                        id="confirm-password-input"
                        name="confirm-password-input"
                        v-model="$v.form.confirmPassword.$model"
                        :state="validateState('confirmPassword')"
                        type="password"
                        aria-describedby="confirm-password-input-feedback"
                        placeholder="* Повторите пароль"
                      ></b-form-input>
                      <b-form-invalid-feedback
                        id="confirm-password-input-feedback"
                      >Должно быть не менее 8 символов.</b-form-invalid-feedback>
                    </b-form-group>
                    </div>

                  <b-button type="submit" variant="w-100 btn btn-lg btn-primary">Зарегистрироваться</b-button>
                </b-form>

          <hr class="my-4">
              <router-link :to="{name: 'SignIn'}">Вход</router-link>
          </div>
    </div>
    </div>
    </div>
    </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, minLength } from 'vuelidate/lib/validators'
// import router from '@/router';

export default {
  name: 'SignUp',
  mixins: [validationMixin],
  data () {
    return {
      form: {
        nickname: null,
        email: null,
        password: null,
        confirmPassword: null
      }
    }
  },
  validations: {
    form: {
      nickname: {
        required,
        minLength: minLength(4)
      },
      email: {
        required
      },
      password: {
        required,
        minLength: minLength(8)
      },
      confirmPassword: {
        required,
        minLength: minLength(8)
      }
    }
  },
  methods: {
    validateState (name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
    },
    resetForm () {
      this.form = {
        name: null,
        email: null,
        password: null,
        confirmPassword: null,
        town: null
      }

      this.$nextTick(() => {
        this.$v.$reset()
      })
    },
    async onSubmit () {
      try {
        const response = await this.axios.post('http://127.0.0.1:8000/auth/users/',
          { 'email': this.form.email, 'username': this.form.nickname, 'password': this.form.password })

        console.log('success', response)
        await this.$store.dispatch('SET_USERNAME', response.data.username)
        await this.$router.push({ name: 'SignIn' })
      } catch (e) {
        console.log(e)
        console.log(e.response)

        if (e.response) {
          this.errors = e.response.data
        }
      }
    }
  }
}
</script>
