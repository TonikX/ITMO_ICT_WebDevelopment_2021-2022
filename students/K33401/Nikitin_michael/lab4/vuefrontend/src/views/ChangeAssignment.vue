<template>

  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Enter service info</h1>

        <form v-on:submit.prevent="change(assignObj.id)">
          <div class="form-group">
            <input type="number" name="appl" v-model="application" class="form-control" placeholder="Application number">
          </div>
          <div class="form-group">
            <input type="boolean" name="is_paid" v-model="is_paid" class="form-control" placeholder="Is paid?">
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
  const baseUrlApi = 'http://127.0.0.1:8000/api/assignment/'
  export default {
    name: 'change_assignment',
    created () {
        this.getObj()
        if (this.$store.state.accessToken == null) {
          alert("You need to login")
          this.$router.push({ name: 'assignments' })
        }
    },
    data () {
      return {
        id: "",
        application: "",
        is_paid: "",
        assignObj: ""
      }
    },
    methods: {

      /**
        * Get chosen assignmment
        * 
        * @returns {Object} - assignmment object
        */
      getObj () {
      $.ajax({
        url: baseUrlApi + this.$route.params.id,
        type: 'GET',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        success: (response) => {
          console.log(response)
          this.assignObj = response
          this.id = this.assignObj.id
          this.application = this.assignObj.application
          this.is_paid = this.assignObj.is_paid
        },
        error: (response) => {
          console.log(response)
        }
      })
    },

    /**
        * Change chosen assignmment
        * 
        * @param {number} id - id of chosen assignmment
        */
    change (id) {
      $.ajax({
        url: baseUrlApi + id + '/update',
        type: 'PUT',
        headers: {Authorization: `Bearer ${this.$store.state.accessToken}`},
        data: {
          id: this.id,
          application: this.application,
          is_paid: this.is_paid,
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'assignments' })
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