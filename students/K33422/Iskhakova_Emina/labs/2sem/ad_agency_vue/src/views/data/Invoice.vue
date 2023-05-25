<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <invoice-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import InvoiceTableCard from '@/components/data/InvoiceTableCard'

export default {
  name: 'Invoice',
  components: {
    InvoiceTableCard
  }
}
</script>

<style scoped>

</style>
