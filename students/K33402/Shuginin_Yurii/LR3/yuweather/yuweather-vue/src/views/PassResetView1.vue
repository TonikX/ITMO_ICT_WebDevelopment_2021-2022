<template>
  <div class="passreset1">
    <SimpleHeader />
    <main>
      <div class="container py-4">
        <PassReset1 />
      </div>
    </main>
    <Footer :bottom="BottomFooter" />
    <PassResetModal />
  </div>
</template>

<script>
import SimpleHeader from '@/components/SimpleHeader.vue'
import Footer from '@/components/Footer.vue'
import PassReset1 from '@/components/PassReset1.vue'
import PassResetModal from '@/components/PassResetModal.vue'

export default {
  name: 'PassResetView1',
  data: () => ({
    BottomFooter: 'bottom'
  }),

  components: {
    SimpleHeader,
    Footer,
    PassReset1,
    PassResetModal
  }
}
</script>
