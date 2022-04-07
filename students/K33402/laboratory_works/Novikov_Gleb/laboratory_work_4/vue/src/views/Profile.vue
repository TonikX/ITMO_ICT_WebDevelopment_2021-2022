<template>
   <div class="bg">
    <div class="container col-xl-10 col-xxl-8 px-4 py-5">
        <div class="row align-items-center g-lg-5 py-5">
          <div class="col-md-10 mx-auto col-lg-5">
        <div class="text">
          <h1 class="display-4 fw-bold lh-1 mb-5 center">👤 Профиль</h1>
          </div>
            <div class="p-4 p-md-5 border rounded-3 bg-light">
              <form class="form-floating mb-4" id="formNickname" >
                <label for="floatingNickname">Ваш никнейм: {{ this.$store.getters.USERNAME }}</label>
                <input v-model="form.nickname" class="form-control" ref="floatingNickname" id="floatingNickname" placeholder="* Новый никнейм">
              </form>
              <form class="form-floating mb-4" id="formEmail" >
                <label for="floatingNickname">Ваш email: {{ this.$store.getters.EMAIL }}</label>
                <input v-model="form.email" class="form-control" ref="floatingEmail" id="floatingEmail" placeholder="* Новый email">
              </form>
              <div class="form-floating mb-4">
                <label for="floatingPassword">Для изменения данных введите ваш пароль</label>
                <input v-model="form.password" type="password" class="form-control" id="floatingPassword" placeholder="* Пароль">
              </div>
              <button class="btn btn-lg btn-primary mt-4" @click="onSubmit">Обновить профиль</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Profile',

  data () {
    return {
      form: {
        nickname: null,
        email: null,
        password: null
      }
    }
  },

  methods: {
    async onSubmit () {
      try {
        const response2 = await this.axios.patch('http://127.0.0.1:8000/auth/users/me/',
          { 'email': this.form.email },
          { headers: { 'Authorization': `Token ${this.$store.state.token}` } })
        console.log('success', response2)
        await this.$store.dispatch('SET_EMAIL', response2.data.email)

        const response1 = await this.axios.post('http://127.0.0.1:8000/auth/users/set_username/',
          { 'new_username': this.form.nickname, 'current_password': this.form.password },
          { headers: { 'Authorization': `Token ${this.$store.state.token}` } })
        await this.$store.dispatch('SET_USERNAME', this.form.nickname)
      } catch (e) {
        console.log(e)
        console.log(e.response)
      }
    }
  }
}

</script>
