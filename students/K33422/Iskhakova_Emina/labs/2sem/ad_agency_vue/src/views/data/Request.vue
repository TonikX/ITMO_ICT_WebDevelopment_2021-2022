<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <request-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import RequestTableCard from '@/components/data/RequestTableCard'

export default {
  name: 'Request',
  components: {
    RequestTableCard
  }
}
</script>

<style scoped>

</style>
