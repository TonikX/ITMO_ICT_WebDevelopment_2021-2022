<template>
  <div class="posts">
    <NavBar></NavBar>
      <div class="album py-5 bg-light">
          <div class="container">
          <router-link :to="{ name:'assignment_create' }" id="crt" class="btn btn-sm btn-outline-success" role="button" aria-pressed="true">Create</router-link>
          <p></p>
            <div class="row">

              <div v-for="assign in APIData" :key="assign.id" class="col-md-4">
                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class=""><router-link :to="{name:'one_assignment', params:{id: assign.id}}">Assignment number: {{ assign.id }}</router-link></h4>
                      <p class="card-text">Is paid: {{assign.is_paid}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                          <v-btn @click="delServ(assign.id)" class="btn btn-sm btn-outline-danger" role="button" aria-pressed="true">Delete</v-btn>
                      <router-link :to="{name:'change_assignment', params:{id: assign.id}}" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">Edit</router-link>
                      </div>
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
  import $ from 'jquery'
  const baseUrlApi = 'http://127.0.0.1:8000/api/assignment/'
  import NavBar from '../components/Navbar'
  export default {
    name: 'posts',
    components: {
      NavBar
    },
    created () {
        this.getObj()
    },
    data () {
      return {
        APIData: ""
      }
    },
    methods: {

      /**
        * Delete chosen assignment
        * 
        * @param {number} id - id of chosen assignment
        */
      delServ(id) {
        $.ajax({
          url: baseUrlApi + id + '/delete',
          type: 'DELETE',
          headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
          success: (response) => {
            alert('Assignment deleted')
            console.log(response)
            this.getObj()
          },
          error: (response) => {
            alert('You need to login')
            console.log(response)
          }
        })
      },

      /**
        * Get all assignments
        * 
        * @returns {List<Object>} - list of assignment objects
        */
      getObj () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/assignments',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.APIData = response
        },
        error: (response) => {
          console.log(response)
          alert('You need to login')
        }
      })
    }
    }
  }
</script>

<style>

</style>
