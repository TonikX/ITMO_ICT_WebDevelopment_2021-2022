<template>
    <div>
        <h1 class="mb-2">Туры</h1>
        <p class="mb-4">Список актуальный туров, выбирайте тот, что вам по душе!</p>
        <ToursList />
    </div>
</template>

<script>
    import ToursList from "@/components/ToursList";
    export default {
        name: "HomePage",
        components: {ToursList},
        mounted: function () {
            this.$store.dispatch('toursList')
        },
    }
</script>

<style scoped>

</style>