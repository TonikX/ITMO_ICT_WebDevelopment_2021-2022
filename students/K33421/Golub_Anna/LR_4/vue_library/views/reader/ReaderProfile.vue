<template>
<div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Личный кабинет</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          Имя: <b>{{ this.reader.first_name }}</b> <br>
          Фамилия: <b>{{ this.reader.last_name }}</b> <br>
          Логин: {{ this.reader.username }} <br>
          Номер билета: {{ this.reader.card_number }} <br>
          Дата рождения: {{ this.reader.date_of_birth }} <br>
          Образование: {{ this.reader.education }} <br>
          Ученая степень: {{ this.reader.degree ? 'есть' : 'нет' }} <br>
          Паспортные данные: {{ this.reader.passport }} <br>
          Адрес: {{ this.reader.address }} <br>
          Телефон: {{ this.reader.phone }} <br>
        </div>
      </v-card-text>
    </v-card>

  <v-card
    elevation="2"
    outlined
    class="my-2">
    <v-card-text class="text--primary">
      Вы сейчас читаете:
      <ul>
          <li v-for="book in reader.reader_book" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>, {{ book.authors }}
          </li>
        </ul>
    </v-card-text>
  </v-card>

  <v-card>
    <v-card-text  style="margin-top:1cm">
      <a @click.prevent="goEdit">Редактировать профиль</a><br>
    </v-card-text>
  </v-card>

    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goCatalogue">Каталог</a><br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'ReaderProfile',

  data () {
    return {
      reader: Object
    }
  },

  created () {
    this.loadReaderData()
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.loadCurrentlyReading()
    },

    async loadCurrentlyReading () {
      this.cur_read_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await this.axios.get(this.cur_read_url)
      this.reader = response.data
      console.log(response)
    },

    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goEdit () {
      this.$router.push({ name: 'reader_profile_edit' })
    }
  }
}
</script>

<style>

</style>
