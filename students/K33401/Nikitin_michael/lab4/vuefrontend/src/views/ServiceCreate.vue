<template>
  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Enter service info</h1>

        <form v-on:submit.prevent="create">
          <div class="form-group">
            <input type="text" name="title" v-model="title" class="form-control" placeholder="Title">
          </div>
          <div class="form-group">
            <input type="number" name="price" v-model="price" class="form-control" placeholder="Price">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Create</button>
        </form>
        
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  const urlApi = 'http://127.0.0.1:8000/api/service/create'
  export default {
    name: 'service_create',
    data () {
      return {
        title: "",
        price: "",
      }
    },
    created () {
        if (this.$store.state.accessToken == null) {
          alert("You need to login")
          this.$router.push({ name: 'posts' })
        }
    },
    methods: {

      /**
        * Create new service
        */
      create () {
      $.ajax({
        url: urlApi,
        type: 'POST',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        data: {
          title: this.title,
          price: this.price,
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'posts' })
        },
        error: (response) => {
          alert("You need to log in")
          console.log(response)
        }
      })
    }
      }
  }
</script>

<style>
body { 
  background-color:#f4f4f4;
}
  .login{
    background-color:#fff;
    margin-top:10%;
  }
  input {
    padding: 25px 10px;
}
</style>