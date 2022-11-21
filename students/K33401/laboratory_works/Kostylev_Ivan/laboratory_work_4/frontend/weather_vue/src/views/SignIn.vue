<template>
   <div class="bg-image">
    <div class="container col-xl-10 col-xxl-8 px-4 py-5">
        <div class="row align-items-center g-lg-5 py-5">
          <div class="col-md-10 mx-auto col-lg-5">
        <div class="text">
          <h1 class="display-4 fw-bold lh-1 mb-1 center">M.Y.Weather</h1>
          <h2 class="display-4 fs-4 mb-3">Weather in your browser</h2>
          </div>
            <div class="p-4 p-md-5 border rounded-3 bg-light">
              <form class="form-floating mb-4" id="formNickname" >
                <input v-model="form.nickname" class="form-control" ref="floatingNickname" id="floatingNickname" placeholder="nickname59">
                <label for="floatingNickname">Nickname</label>
              </form>
              <div class="form-floating mb-4">
                <input v-model="form.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
              </div>
              <div class="checkbox mb-3">
                <label>
                  <input type="checkbox" value="remember-me"> Remember me
                </label>
              </div>
              <!-- <form> -->
                  <button class="w-100 btn btn-lg btn-primary" @click="onSubmit">Log in</button>
              <!-- </form> -->
              <hr class="my-4">
              <small class="text-muted">If you don't have an account, <router-link to="/signup">register</router-link></small>
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

<style>
.bg-image {
    background: url('../assets/sky-background.jpg') no-repeat center center fixed;
    background-size: cover;
    min-height:100vh;
}
</style>
