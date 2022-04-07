<template>
  <div class="posts">
    <NavBar></NavBar>
      <div class="album py-5 bg-light">
          <div class="container">
          <router-link :to="{ name:'service_create' }" id="crt" class="btn btn-sm btn-outline-success" role="button" aria-pressed="true">Create</router-link>
          <p></p>
            <div class="row">

                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class="">{{ servObj.title }}</h4>
                      <p class="card-text">{{servObj.price}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                          <v-btn @click="delServ(servObj.id)" class="btn btn-sm btn-outline-danger" role="button" aria-pressed="true">Delete</v-btn>
                      <router-link :to="{name:'change_service', params:{id: servObj.id}}" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">Edit</router-link>
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
  const baseUrlApi = 'http://127.0.0.1:8000/api/service/'
  export default {
    name: 'one_service',
    components: {
      NavBar
    },
    created () {
        this.getObj()
        if (this.$store.state.accessToken == null) {
          alert("You need to login")
          this.$router.push({ name: 'posts' })
        }
    },
    data () {
      return {
        id: "",
        title: "",
        price: "",
        servObj: ""
      }
    },
    methods: {

      /**
        * Get chosen service
        * 
        * @returns {Object} - service object
        */
      getObj () {
      $.ajax({
        url: baseUrlApi + this.$route.params.id,
        type: 'GET',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        success: (response) => {
          console.log(response)
          this.servObj = response
          this.id = this.servObj.id
          this.title = this.servObj.title
          this.price = this.servObj.price
        },
        error: (response) => {
          console.log(response)
        }
      })
    },
    delServ(id) {
        $.ajax({
          url: baseUrlApi + id + '/delete',
          type: 'DELETE',
          headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
          success: (response) => {
            alert('Service deleted')
            console.log(response)
            this.$router.push({ name: 'posts' })
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
