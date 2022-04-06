<template>
    <div class="row mx-auto justify-content-center mt-3">
        <div class="col-xxl-4 col-xl-5 col-lg-6 col-md-8 col-sm-10 col-12">
            <form action="" class="d-flex flex-column" @submit="edit_data">
                <label for="username" class="text-primary"><h6>Username</h6></label>
                <input v-model="username" class="form-control border-primary text-primary mb-3" type="text" id="username" style="background-color: white" disabled>
                <!-- <label for="password" class="text-primary"><h6>Password</h6></label>
                <input class="form-control border-white text-primary mb-3" type="password" id="password" :value="password" style="background-color: white" disabled> -->
                <label for="email" class="text-primary"><h6>E-mail</h6></label>
                <input v-model="email" class="form-control border-primary text-primary mb-3" type="email" id="email" required>
                <label for="name" class="text-primary"><h6>Name</h6></label>
                <input v-model="first_name" class="form-control border-primary text-primary mb-3" type="text" id="name">
                <label for="surname" class="text-primary"><h6>Surname</h6></label>
                <input v-model="last_name" class="form-control border-primary text-primary mb-4" type="text" id="surname">
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary btn-lg px-5">Save</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
  name: 'ProfileEditForm',

  data: () => ({
    username: '',
    email: '',
    first_name: '',
    last_name: ''
  }),

  methods: {
    edit_data (event) {
      event.preventDefault()

      this.axios
        .patch('http://localhost:8000/auth/users/me/', {
          username: this.username,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        },
        { headers: { Authorization: `Token ${localStorage.getItem('token')}` } }
        )
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    }
  },

  created () {
    if (localStorage.getItem('token')) {
      this.axios
        .get('http://localhost:8000/auth/users/me/', { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        .then(response => {
          this.username = response.data.username
          this.email = response.data.email
          this.first_name = response.data.first_name
          this.last_name = response.data.last_name
        })
        .catch(err => {
          console.error(err)
          window.location.href = 'error?back=1'
        })
    } else {
      this.$router.push('/login')
    }
  }
}
</script>

<style>
</style>
