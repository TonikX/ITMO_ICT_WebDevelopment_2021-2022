<template>
  <div>
    <h1 class="black--text mt-0 pt-0 mb-10">PROFILE</h1>
    <v-row>
      <v-col cols="3" class="mx-auto">
        <v-card
            elevation="5"
            outlined
            v-if="!change">
          <p class="pt-5"> <b class="black--text">Username:</b> {{username}} </p>
          <p> <b class="black--text">Full name:</b> {{ userForm.full_name }} </p>
          <p> <b class="black--text">Experience:</b> {{ userForm.experience }} </p>
          <p class="pb-4"> <b class="black--text">Email:</b> {{userForm.email}} </p>
        </v-card>
        <v-form
            @submit.prevent="changeUser"
            ref="userForm"
            v-if="change"
        >
          <v-text-field
              label="Full name"
              v-model="userForm.full_name"
          />
          <v-text-field
              label="Experience"
              v-model="userForm.experience"
          />
          <v-text-field
              label="Email"
              v-model="userForm.email"
          />
          <v-btn type="submit" color="orange darken-1" dark>Accept</v-btn>
        </v-form>
        <v-btn
            @click="openForm()"
            class="my-3"
            style="width: 100px"
            color="orange darken-1"
            dark
            v-if="!change"
        >
          Update
        </v-btn>
        <br>
        <v-btn
            @click="showDelete()"
            class="v-list-item--link"
            color="red darken-4"
            dark
            v-if="!toDelete"
        >
          Delete
        </v-btn>
        <v-form
            v-if="toDelete"
            @submit.prevent="deleteUser"
        >
          <v-text-field
              label="Введите пароль для подтверждения"
              v-model="password"
              type="password"
          />
          <v-btn type="submit" color="red darken-4" dark>Accept</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const host = 'http://127.0.0.1:8000/'
export default {
  name: 'Home',
  data: () => ({
    username: '',
    userForm: {
      full_name: '',
      experience: '',
      email: '',
      username: ''
    },
    change: false,
    toDelete: false,
    password: ''
  }),
  methods: {
    getParameters () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        this.axios
            .get(`${host}auth/users/me/`)
            .then(response => {
              this.username = response.data.username
              this.userForm.full_name = response.data.full_name
              this.userForm.experience = response.data.experience
              this.userForm.email = response.data.email
            })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    openForm () {
      this.change = true
    },
    changeUser () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.userForm)
        const response = this.axios
            .patch(`${host}auth/users/me/`, this.userForm)
            .then(resp => {
              this.change = false
              this.getParameters()
              this.$refs.userForm.reset()
              return resp
            })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.userForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    showDelete () {
      this.toDelete = true
    },
    deleteUser () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.password)
        this.axios
            .delete(`${host}auth/users/me/`, { data: { current_password: this.password } })
            .then(resp => {
              this.change = false
              localStorage.removeItem('token')
              this.toDelete = false
              this.$bus.$emit('logged', 'User deleted')
              this.$router.push('/login')
              return resp
            })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.getParameters()
  }
}
</script>

<style scoped>
p {
  text-align: left;
  padding-left: 25px;
}
</style>
