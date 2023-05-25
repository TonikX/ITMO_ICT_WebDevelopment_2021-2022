<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <executor-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ExecutorTableCard from '@/components/data/ExecutorTableCard'

export default {
  name: 'Executor',
  components: {
    ExecutorTableCard
  }
}
</script>

<style scoped>

</style>
