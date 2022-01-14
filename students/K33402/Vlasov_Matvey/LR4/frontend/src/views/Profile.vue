<template>
    <main role="main">
        <b-container class="pt-4">
            <template v-if="!this.$store.state.isLogged">
                <b-alert show>
                You have no right to view this information.
                You can only see your students submissions
            </b-alert>
            </template>
            <template v-else>
                <div class="d-flex justify-content-center">
                    <h2>My Profile</h2>
                </div>
                <profile-form />
            </template>
        </b-container>
    </main>
</template>

<script>
import ProfileForm from '@/components/ProfileForm.vue'

export default {
    name: 'Profile',
    components: {
        ProfileForm
    }
}
</script>
