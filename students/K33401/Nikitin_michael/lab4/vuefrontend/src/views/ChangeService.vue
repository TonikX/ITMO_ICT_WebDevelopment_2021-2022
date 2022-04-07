<template>

  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Enter service info</h1>

        <form v-on:submit.prevent="change(servObj.id)">
          <div class="form-group">
            <input type="text" name="title" v-model="title" class="form-control" placeholder="Title">
          </div>
          <div class="form-group">
            <input type="number" name="price" v-model="price" class="form-control" placeholder="Price">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Change</button>
        </form>
        
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  const baseUrlApi = 'http://127.0.0.1:8000/api/service/'
  export default {
    name: 'change_service',
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
    change (id) {
      $.ajax({
        url: baseUrlApi + id + '/update',
        type: 'PUT',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        data: {
          id: this.id,
          title: this.title,
          price: this.price,
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'posts' })
        },
        error: (response) => {
          alert(response)
          console.log(response)
        }
      })
    },
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