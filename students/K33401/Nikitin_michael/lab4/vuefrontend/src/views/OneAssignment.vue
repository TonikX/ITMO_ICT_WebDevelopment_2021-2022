<template>
  <div class="posts">
    <NavBar></NavBar>
      <div class="album py-5 bg-light">
          <div class="container">
          <router-link :to="{ name:'assignment_create' }" id="crt" class="btn btn-sm btn-outline-success" role="button" aria-pressed="true">Create</router-link>
          <p></p>
            <div class="row">

                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class="">Assignment number: {{ assignObj.id }}</h4>
                      <p class="card-text">Is paid: {{assignObj.is_paid}}</p>
                      <p>Total price: {{ applObj.price }}р.</p>
                      <p>Total price: {{ servObj.title }}</p>

                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                          <v-btn @click="delAssign(assignObj.id)" class="btn btn-sm btn-outline-danger" role="button" aria-pressed="true">Delete</v-btn>
                      <router-link :to="{name:'change_assignment', params:{id: assignObj.id}}" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">Edit</router-link>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  import $ from 'jquery'
  const baseUrlApi = 'http://127.0.0.1:8000/api/assignment/'
  export default {
    name: 'one_service',
    components: {
      NavBar
    },
    created () {
        this.getObj()
        this.getAppOfAssign()
        this.getServOfAssign()

    },
    data () {
      return {
        id: "",
        title: "",
        price: "",
        assignObj: "",
        applObj: "",
        servObj: ""
      }
    },
    methods: {
      getObj () {
      $.ajax({
        url: baseUrlApi + this.$route.params.id,
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.assignObj = response
          this.id = this.assignObj.id
          this.application = this.assignObj.application
          this.is_paid = this.assignObj.is_paid
          sessionStorage.setItem('appl', this.application)
        },
        error: (response) => {
          console.log(response)
        }
      })
    },
    delAssign(id) {
        $.ajax({
          url: baseUrlApi + id + '/delete',
          type: 'DELETE',
          headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
          success: (response) => {
            alert('Assignment deleted')
            console.log(response)
            this.$router.push({ name: 'assignments' })
          },
          error: (response) => {
            console.log(response)
          }
        })
      },
    getAppOfAssign() {
      $.ajax({
        url: `http://127.0.0.1:8000/api/applications/${sessionStorage.getItem('appl')}`,
        type: 'GET',
        success: (response) => {
            console.log(response)
            this.applObj = response
            this.service = this.applObj.service
            sessionStorage.setItem('serv', this.service)
          },
          error: (response) => {
            console.log(response)
          }
      })
    },
    getServOfAssign() {
      $.ajax({
        url: `http://127.0.0.1:8000/api/service/${sessionStorage.getItem('serv')}`,
        type: 'GET',
        success: (response) => {
            console.log(response)
            this.servObj = response
          },
          error: (response) => {
            console.log(response)
          }
      })
    }
    }
  }
</script>

<style>

</style>
