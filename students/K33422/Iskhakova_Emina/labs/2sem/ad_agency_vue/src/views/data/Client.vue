<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <client-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ClientTableCard from '@/components/data/ClientTableCard'

export default {
  name: 'Client',
  components: {
    ClientTableCard
  }
}
</script>

<style scoped>

</style>
