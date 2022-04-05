<template>
  <div>
    <h1 class="black--text mt-0 pt-0 mb-7">Личный кабинет</h1>
    <v-row>
      <v-col cols="3" class="mx-auto">
        <h3 class="black--text mt-0 pt-0 mb-7">Информация</h3>
        <v-card v-if="!change">
          <p class="pt-5"> <b class="black--text">Username:</b> {{username}} </p>
          <p> <b class="black--text">FIO:</b> {{ userForm.fio }} </p>
          <p> <b class="black--text">Stajh raboty:</b> {{ userForm.stajh_raboty }} </p>
          <p class="pb-5"> <b class="black--text">Email:</b> {{userForm.email}} </p>
        </v-card>
        <v-form
          @submit.prevent="changeUser"
          ref="userForm"
          v-if="change"
        >
          <v-text-field
            label="FIO"
            v-model="userForm.fio"
          />
          <v-text-field
            label="Stajh raboty"
            v-model="userForm.stajh_raboty"
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
        <v-btn
          @click="openForm()"
          class="my-3"
          style="width: 100px"
          color="black"
          dark
          v-if="!change"
        >
          Изменить
        </v-btn>
        <br>
        <v-btn
          @click="showDelete()"
          class="v-list-item--link"
          v-if="!toDelete"
        >
          Удалить профиль
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
          <v-btn type="submit" color="black" dark>Принять</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const host = 'http://127.0.0.1:8000/'
export default {
  name: 'PersonalPage',
  data: () => ({
    username: '',
    userForm: {
      fio: '',
      stajh_raboty: '',
      email: '',
      username: ''
    },
    change: false,
    toDelete: false,
    password: ''
  }),
  methods: {
    getParametrs () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        this.axios
          .get(`${host}auth/users/me/`)
          .then(response => {
            this.username = response.data.username
            this.userForm.fio = response.data.fio
            this.userForm.stajh_raboty = response.data.stajh_raboty
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
            this.getParametrs()
            this.$refs.userForm.reset()
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
            this.$router.push('/signin')
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.getParametrs()
  }
}
</script>

<style scoped>
  p {
    text-align: left;
    padding-left: 25px;
  }
</style>
