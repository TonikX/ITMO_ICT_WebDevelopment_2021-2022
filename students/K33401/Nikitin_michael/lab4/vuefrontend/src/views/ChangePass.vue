<template>
  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Enter new password</h1>

        <form v-on:submit.prevent="change">
          <div class="form-group">
            <input type="text" name="old_password" v-model="old_password" class="form-control" placeholder="Old password">
          </div>
          <div class="form-group">
            <input type="text" name="new_password" v-model="new_password" class="form-control" placeholder="New password">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Reset password</button>
        </form>
        
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: 'change_password',
    data () {
      return {
        old_password: "",
        new_password: ""
      }
    },
    methods: {
      change () { 
        $.ajax({
          url: 'http://127.0.0.1:8000/api/change-password',
          type: 'PUT',
          headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
          data: {
            old_password: this.old_password,
            new_password: this.new_password
          },
          success: (response) => {
            console.log(response)
            this.$router.push({name: 'login'})
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