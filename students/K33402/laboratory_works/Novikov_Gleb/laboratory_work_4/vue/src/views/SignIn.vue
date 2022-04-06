<template>
   <div class="bg">
    <div class="container col-xl-10 col-xxl-8 px-4 py-5">
        <div class="row align-items-center g-lg-5 py-5">
          <div class="col-md-10 mx-auto col-lg-5">
        <div class="text">
          <h1 class="display-4 fw-bold lh-1 mb-5 center">Вход</h1>
          </div>
            <div class="p-4 p-md-5 border rounded-3 bg-light">
              <form class="form-floating mb-4" id="formNickname" >
                <input v-model="form.nickname" class="form-control" ref="floatingNickname" id="floatingNickname" placeholder="* Имя пользователя">
              </form>
              <div class="form-floating mb-4">
                <input v-model="form.password" type="password" class="form-control" id="floatingPassword" placeholder="* Пароль">
              </div>
              <button class="btn btn-lg btn-primary mt-4" @click="onSubmit">Войти</button>
              <hr class="my-4">
              <router-link to="/signup">Регистрация</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'SignIn',

  data () {
    return {
      form: {
        nickname: null,
        password: null
      }
    }
  },

  methods: {
    async onSubmit () {
      try {
        const response = await this.axios.post('http://127.0.0.1:8000/auth/token/login/',
          { 'username': this.form.nickname, 'password': this.form.password })

        console.log('success', response)
        await this.$store.dispatch('SET_TOKEN', response.data.auth_token)
        await this.$store.dispatch('SET_USERNAME', this.form.nickname)
        await this.$router.push({ name: 'Weather' })
      } catch (e) {
        console.log(e)
        console.log(e.response)
      }
    }
  }
}

</script>
