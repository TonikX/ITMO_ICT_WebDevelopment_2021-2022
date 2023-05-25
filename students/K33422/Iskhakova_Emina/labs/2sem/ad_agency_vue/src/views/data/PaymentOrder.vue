<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <payment-order-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import PaymentOrderTableCard from '@/components/data/PaymentOrderTableCard'

export default {
  name: 'PaymentOrder',
  components: {
    PaymentOrderTableCard
  }
}
</script>

<style scoped>

</style>
