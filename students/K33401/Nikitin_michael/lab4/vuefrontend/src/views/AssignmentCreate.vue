<template>
  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Enter service info</h1>

        <form v-on:submit.prevent="create">
          <div class="form-group">
            <input type="number" name="appl" v-model="application" class="form-control" placeholder="Application number">
          </div>
          <div class="form-group">
            <input type="boolean" name="is_paid" v-model="is_paid" class="form-control" placeholder="Is paid?">
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
  const urlApi = 'http://127.0.0.1:8000/api/assignment/create'
  export default {
    name: 'assignment_create',
    data () {
      return {
        application: "",
        is_paid: "",
      }
    },
    created () {
        if (this.$store.state.accessToken == null) {
          alert("You need to login")
          this.$router.push({ name: 'assignments' })
        }
    },
    methods: {
      create () {
      $.ajax({
        url: urlApi,
        type: 'POST',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        data: {
          application: this.application,
          id_paid: this.is_paid,
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'assignments' })
        },
        error: (response) => {
          alert("You need to login")
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