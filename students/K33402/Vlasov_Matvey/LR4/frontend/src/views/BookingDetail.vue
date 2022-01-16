<template>
    <main role="main">
        <b-container class="py-4">
            <booking-card-detail :booking-item="this.$route.params.item" />
        </b-container>
    </main>
</template>

<script>
import BookingCardDetail from '@/components/BookingCardDetail.vue'

export default {
    name: 'BookingDetail',
    components: {
        BookingCardDetail
    }
}
</script>
