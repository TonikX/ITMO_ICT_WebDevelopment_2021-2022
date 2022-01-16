<template>
    <main role="main">
        <b-container class="py-4">
            <property-card-detail :property-item="this.$route.params.item" />
        </b-container>
    </main>
</template>

<script>
import PropertyCardDetail from '@/components/PropertyCardDetail.vue'

export default {
    name: 'PropertyDetail',
    components: {
        PropertyCardDetail
    }
}
</script>
