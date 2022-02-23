<template>
    <b-col cols="6" class="mx-auto border p-3 rounded">
        <sign-up-form />
    </b-col>
</template>

<script>
    import SignUpForm from '@/components/auth/SignUpForm.vue'

    export default {
        name: "SignUpPage",
        components: { SignUpForm }
    }
</script>

<style scoped>

</style>