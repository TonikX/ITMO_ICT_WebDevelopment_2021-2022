<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <chosen-services-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ChosenServicesTableCard from '@/components/data/ChosenServicesTableCard'

export default {
  name: 'ChosenServices',
  components: {
    ChosenServicesTableCard
  }
}
</script>

<style scoped>

</style>
