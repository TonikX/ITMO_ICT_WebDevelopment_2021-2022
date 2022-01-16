<template>
  <div>
    <v-row>
      <v-col cols="3" class="mx-auto">
        <h3 class="black--text mt-0 pt-0 mb-7">Info</h3>
        <br/>
        <v-card v-if="!change">
          <p class="pt-5"><b class="black--text">Username:</b> {{ username }} </p>
          <p><b class="black--text">First Name:</b> {{ userForm.first_name }} </p>
          <p><b class="black--text">Last Name:</b> {{ userForm.last_name }} </p>
          <p class="pb-5"><b class="black--text">Email:</b> {{ userForm.email }} </p>
        </v-card>
        <br/>
        <v-form
            @submit.prevent="changeUser"
            ref="userForm"
            v-if="change"
            class="profile-form"
        >
          <v-text-field
              label="First Name"
              v-model="userForm.first_name"
          />
          <v-text-field
              label="Last Name"
              v-model="userForm.last_name"
          />
          <v-text-field
              label="email"
              v-model="userForm.email"
          />
          <v-text-field
              label="Username"
              v-model="userForm.username"
          />
          <v-btn type="submit" color="black" dark>Принять</v-btn>
        </v-form>

        <div class="btn-container">
          <v-btn
              @click="openForm()"
              class="my-3"
              style="width: 100px"
              color="blue darken-2"
              dark
              v-if="!change"
          >
            Edit
          </v-btn>
          <br>
          <v-btn
              @click="showDelete()"
              class="v-list-item--link"
              v-if="!toDelete"
              color="black"
              dark
          >
            Delete profile
          </v-btn>
        </div>
        <v-form
            v-if="toDelete"
            @submit.prevent="deleteUser"
        >
          <v-text-field
              label="Введите пароль для подтверждения"
              v-model="password"
              type="password"
          />
          <v-btn type="submit" color="red" dark>Принять</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const host = 'http://127.0.0.1:8000/'
export default {
  name: 'Profile',
  data: () => ({
    username: '',
    userForm: {
      first_name: '',
      last_name: '',
      email: '',
      username: ''
    },
    change: false,
    toDelete: false,
    password: ''
  }),
  methods: {
    getParametrs() {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        this.axios
            .get(`${host}auth/users/me/`)
            .then(response => {
              this.username = response.data.username
              this.userForm.first_name = response.data.first_name
              this.userForm.last_name = response.data.last_name
              this.userForm.email = response.data.email
            })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    openForm() {
      this.change = true
    },
    changeUser() {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.userForm)
        const response = this.axios
            .patch(`${host}auth/users/me/`, this.userForm)
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.userForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    showDelete() {
      this.toDelete = true
    },
    deleteUser() {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.password)
        this.axios
            .delete(`${host}auth/users/me/`, {data: {current_password: this.password}})
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created() {
    this.getParametrs()
  }
}
</script>

<style scoped>
p {
  text-align: left;
  padding-left: 25px;
}

.profile-form {

}

.btn-container {
  display: flex;
  justify-content: space-between;
  gap: 10px
}
</style>