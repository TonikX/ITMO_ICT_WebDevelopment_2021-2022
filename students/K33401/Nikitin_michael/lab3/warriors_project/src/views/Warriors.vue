<template>
  <div class="posts">
    <!--<Navbar></Navbar>-->
      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="posts in APIData" :key="posts.id" class="col-md-4">
                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class=""><div class="text-secondary" href="">{{posts.name}} {{posts.surname}}</div></h4>
                      <p class="card-text">ph: {{posts.phone}}</p>
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
  import Navbar from '../components/Navbar'
  const host = 'http://127.0.0.1:8000/'
  export default {
    name: 'warriors',
    components: {
      Navbar
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

      getObj () {
        const response = this.axios
          .get(`${host}war/warriors/`)

       /* if (response.status !== 200) {
          throw new Error(response.error)
        }
*/
        console.log(response.data)

        this.orderItems = response.data.map((orderItem) => {
          console.log(orderItem)
          return orderItem
        });
       // catch (e) {
       // console.error('AN API ERROR', e)
      }
    }
  }
</script>