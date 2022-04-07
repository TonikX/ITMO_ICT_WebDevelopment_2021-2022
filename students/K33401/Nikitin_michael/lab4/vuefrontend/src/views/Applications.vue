<template>
  <div class="posts">
    <NavBar></NavBar>
      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="posts in Applications" :key="posts.id" class="col-md-4">
                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class=""><div class="text-secondary" href="">{{posts.service}}</div></h4>
                      <p class="card-text">{{posts.price}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
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
  import NavBar from '../components/Navbar'

  export default {
    name: 'applications',
    components: {
      NavBar
    },
    created () {
        this.getApplications()
    },
    data () {
      return {
        Applications: []
      }
    },
    methods: {
      /**
        * Get all applications
        */
      getApplications () {
          try {
              this.$http
                  .get('http://127.0.0.1:8000/applications')
                  .then(response => this.setApplications(response))
          } catch(e) {
              console.log(e.toString())
          }
      },
      setApplications(response) {
          this.Applications = response
      }
    }
  }
</script>
