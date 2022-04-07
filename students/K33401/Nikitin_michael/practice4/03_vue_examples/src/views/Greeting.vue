<template>
 <section>
   <v-container>
     <greeting-card :username="savedUsername" />
 
   <h2>Это простой проект на Vue.</h2>
   <v-form @submit.prevent="submitUsername">
     <v-row>
       <v-col cols="3" class="mx-auto">
         <v-text-field
           label="Введите своё имя"
           v-model="username"
           name="username"
           placeholder="Иван Иванов"
         />
       </v-col>
     </v-row>
   </v-form>

   <h3>Варианты приветствий:</h3>

   <v-row>
     <v-col cols="4" class="mx-auto">
       <v-card
         elevation="2"
         class="px-2 py-5"
         color="primary"
         dark
       >
         <greeting-list :greetings="greetings" />
       </v-card>
     </v-col>
   </v-row>
   </v-container>
 </section>
</template>
 
<script>
import GreetingCard from '@/components/GreetingCard'
import GreetingList from '../components/GreetingList'
 
export default {
 name: 'Greeting',
 
 components: {
   GreetingCard,
   GreetingList
 },
   data: () => ({
    username: '',
    savedUsername: '',
    greetings: [
      { id: 1, text: 'Привет!' },
      { id: 2, text: 'Hello' },
      { id: 3, text: 'Hola' }
    ]
  }),
  methods: {
    submitUsername() {
      localStorage.setItem('username', this.username)
      this.savedUsername = this.username
      this.$refs.from.reset()
    }
  },
  created() {
    if (localStorage.getItem('username')) {
      this.savedUsername = localStorage.getItem('username')
      this.username = this.savedUsername
    }
  }
}
</script>
<style>
.greeting-list-wrapper {
  display: flex;
}

.greeting-list-wrapper .greeting-list {
  margin: auto;
}
</style>