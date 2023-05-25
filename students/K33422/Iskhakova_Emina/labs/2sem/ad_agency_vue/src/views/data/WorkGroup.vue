<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <work-group-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import WorkGroupTableCard from '@/components/data/WorkGroupTableCard'

export default {
  name: 'WorkGroup',
  components: {
    WorkGroupTableCard
  }
}
</script>

<style scoped>

</style>
