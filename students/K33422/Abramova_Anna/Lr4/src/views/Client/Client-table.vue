<template>
	<div class="container">
		<h3>Клиенты</h3>
		<hr>
		<client-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:full_name="item.full_name"
			:pasport="item.pasport"
			:city="item.city"
		/>
		<a href="/client/create" class="btn btn-success">Добавить</a>
	</div>
</template>

<script>
import axios from 'axios'
import ClientRow from '../../components/Client/Client-row'

export default {
	components: { ClientRow },
	name: 'ClientTable',
	data () {
		return {
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/clients/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.items = response.data
		})
	}
}
</script>

<style>

</style>
