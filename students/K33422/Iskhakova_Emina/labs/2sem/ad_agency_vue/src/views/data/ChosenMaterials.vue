<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <chosen-materials-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ChosenMaterialsTableCard from '@/components/data/ChosenMaterialsTableCard'

export default {
  name: 'ChosenMaterials',
  components: {
    ChosenMaterialsTableCard
  }
}
</script>

<style scoped>

</style>
