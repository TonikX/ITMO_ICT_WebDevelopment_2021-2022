<template>
    <div class="row mx-auto justify-content-center">
        <div class="col-xl-4 col-lg-6 col-md-8 col-sm-10 col-12">
            <div class="card border-primary">
                <div class="card-body text-primary">
                    <h4 class="card-title text-center">Authorization</h4>
                    <form action="" class="d-flex flex-column" @submit="login">
                        <input v-model="username" class="form-control border-primary text-primary mt-2 mb-2" type="text" placeholder="Username" required>
                        <input v-model="password" class="form-control border-primary text-primary mb-3" type="password" placeholder="Password" required>
                        <div class="d-flex flex-sm-row flex-column justify-content-between">
                            <div class="form-check d-flex justify-content-center">
                                <input class="form-check-input border-primary me-2" type="checkbox" id="gridCheck1">
                                <label class="form-check-label" for="gridCheck1">Remember me</label>
                            </div>
                            <a href="password_reset" class="text-decoration-none text-center mt-1 mt-sm-0">Forgot password</a>
                        </div>
                        <button type="submit" class="btn btn-primary mt-3 mb-2">Log in</button>
                        <a class="btn btn-outline-primary mb-1" href="registration" role="button">Create a new account</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LoginForm',

  data: () => ({
    username: '',
    password: ''
  }),

  methods: {
    login (event) {
      event.preventDefault()

      this.axios
        .post('http://localhost:8000/auth/token/login/', { username: this.username, password: this.password })
        .then(response => { this.setLogined(response.data.auth_token) })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    },

    setLogined (token) {
      localStorage.setItem('token', token)

      this.axios
        .get('http://localhost:8000/auth/users/me/', { headers: { Authorization: `Token ${token}` } })
        .then(response => {
          localStorage.setItem('user_id', response.data.id)
          window.location.href = '/'
        })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    }
  }
}
</script>

<style>
</style>
