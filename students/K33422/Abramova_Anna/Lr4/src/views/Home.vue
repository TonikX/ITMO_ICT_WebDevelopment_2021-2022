<template>
	<login v-if="!is_auth" />
	<admin-panel v-else/>
</template>

<script>
import Login from '../components/Login.vue'
import AdminPanel from '../components/Admin-panel'

export default {
	components: { Login, AdminPanel },
	name: 'Home',
	data () {
		return {
			is_auth: false
		}
	},
	mounted () {
		this.is_auth = Boolean(sessionStorage.getItem('auth_token') !== null)
	}
}
</script>

<style>

</style>
