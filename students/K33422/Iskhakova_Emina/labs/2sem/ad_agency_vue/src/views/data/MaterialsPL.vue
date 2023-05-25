<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <materials-p-l-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MaterialsPLTableCard from '@/components/data/MaterialsPLTableCard'

export default {
  name: 'MaterialsPL',
  components: {
    MaterialsPLTableCard
  }
}
</script>

<style scoped>

</style>
