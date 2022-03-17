<template>
<router-view></router-view>
</template>
<script>
import PeakList from '../components/PeakList.vue'
import UpdatePeak from '../components/UpdatePeak.vue'

export default {
  mounted () {
    console.log(this.$route)
  },
  name: 'Peak',
  Components: {
    PeakList,
    UpdatePeak
  }
}
</script>
