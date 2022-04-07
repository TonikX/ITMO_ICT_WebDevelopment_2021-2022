<template>
  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Please sign in</h1>

        <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
        <form v-on:submit.prevent="login">
          <div class="form-group">
            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
          </div>
          <div class="form-group">
            <input type="text" name="password" id="pass" v-model="password" class="form-control" placeholder="Password">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
        </form>

      </div>
    </div>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: "",
        password: "",
      }
    },
    methods: {
      logIn () {
        try {
        this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', {
            username: this.username,
            password: this.password
          }).then(response => { this.setLogIn(response) })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
        }
      },
    setLogIn (response) {
      console.log(this.username)
      console.log(this.password)
      localStorage.setItem('token', response.data.auth_token)
      this.$bus.$emit('logged', 'User logged')
      // this.username = ''
      // this.password = ''
      // this.$refs.form.reset()
      this.$router.push('/OneService')
    }
  }

</script>

<style>
body {
  background-color:#f4f4f4;
}
  .login{
    background-color:#fff;
    margin-top:10%;
  }
  input {
    padding: 25px 10px;
}
</style>
