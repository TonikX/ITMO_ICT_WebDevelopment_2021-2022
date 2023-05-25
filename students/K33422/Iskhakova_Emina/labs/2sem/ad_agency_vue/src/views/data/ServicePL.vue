<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <services-p-l-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ServicesPLTableCard from '@/components/data/ServicesPLTableCard'

export default {
  name: 'ServicePL',
  components: {
    ServicesPLTableCard
  },
  data: () => ({
    checked_types: []
  }),
  methods: {
    checkboxSearch () {
      this.axios
        .get(`http://127.0.0.1:8000/ad_agency/servicespl/filter/?service_type=${this.checked_types[0]}`)
        .then((res) => {
          this.service = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>

</style>
