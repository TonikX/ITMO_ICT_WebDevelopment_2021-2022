<template>
  <div class="passreset2">
    <SimpleHeader />
    <main>
      <div class="container py-4">
        <PassReset2 />
      </div>
    </main>
    <Footer :bottom="BottomFooter" />
    <PassRenewModal />
  </div>
</template>

<script>
import SimpleHeader from '@/components/SimpleHeader.vue'
import Footer from '@/components/Footer.vue'
import PassReset2 from '@/components/PassReset2.vue'
import PassRenewModal from '@/components/PassRenewModal.vue'

export default {
  name: 'PassResetView2',
  data: () => ({
    BottomFooter: 'bottom'
  }),

  components: {
    SimpleHeader,
    Footer,
    PassReset2,
    PassRenewModal
  }
}
</script>
