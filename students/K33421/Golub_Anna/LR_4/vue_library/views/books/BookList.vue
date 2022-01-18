<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Каталог библиотеки</h2>
      </v-card-title>
      <v-card-text>
        <ul>
          <li v-for="book in books" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>
          </li>
        </ul>
      </v-card-text>
    </v-card>
    <v-card>
      <v-card-text style="margin-top:2cm">
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'BookList',
  data () {
    return {
      books: ''
    }
  },

  created () {
    // $.ajaxSetup({ headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') } })
    this.loadBooks()
  },

  methods: {
    loadBooks () {
      $.ajax({
        url: 'http://127.0.0.1:8000/library/books/',
        type: 'GET',
        success: (response) => {
          this.books = response
        }
      })
    },

    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style>
</style>
